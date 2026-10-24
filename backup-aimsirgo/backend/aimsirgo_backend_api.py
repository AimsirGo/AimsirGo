from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import Dict, Any, List

app = FastAPI(
    title="AimsirGo API",
    description="Weather-resilient transit routing backend with live weather integration and shelter geodata.",
    version="0.1.0",
)

# Enable CORS for local cross-origin communication with frontend client
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# Mock dataset for local failover and offline testing
MOCK_STOPS_DATA: Dict[str, List[Dict[str, Any]]] = {
    "galway": [
        {"id": "g1", "name": "Eyre Square (Sheltered Hub)", "lat": 53.2743, "lng": -9.0492, "shelter": True, "routes": "401, 402, 404", "transfers": 4},
        {"id": "g2", "name": "University Rd (NUI Galway)", "lat": 53.2781, "lng": -9.0602, "shelter": True, "routes": "404", "transfers": 2},
        {"id": "g3", "name": "Salthill Promenade", "lat": 53.2592, "lng": -9.0760, "shelter": False, "routes": "401", "transfers": 0},
        {"id": "g4", "name": "Cathedral Stop", "lat": 53.2758, "lng": -9.0573, "shelter": True, "routes": "402, 405", "transfers": 3},
        {"id": "g5", "name": "Claddagh Exposed Stop", "lat": 53.2691, "lng": -9.0581, "shelter": False, "routes": "401", "transfers": 1},
        {"id": "g6", "name": "Newcastle Rd Open Stop", "lat": 53.2820, "lng": -9.0640, "shelter": False, "routes": "405", "transfers": 1}
    ],
    "dublin": [
        {"id": "d1", "name": "O'Connell St Upper", "lat": 53.3522, "lng": -6.2608, "shelter": True, "routes": "46A, 140, 155", "transfers": 8},
        {"id": "d2", "name": "Trinity College Gate", "lat": 53.3444, "lng": -6.2592, "shelter": True, "routes": "15, 39A", "transfers": 6},
        {"id": "d3", "name": "Merrion Square West", "lat": 53.3398, "lng": -6.2491, "shelter": False, "routes": "4, 7", "transfers": 1},
        {"id": "d4", "name": "Heuston Station Bay 3", "lat": 53.3465, "lng": -6.2912, "shelter": True, "routes": "C1, C2, C3", "transfers": 10},
        {"id": "d5", "name": "Docklands Uncovered Stop", "lat": 53.3478, "lng": -6.2389, "shelter": False, "routes": "151", "transfers": 0}
    ],
    "cork": [
        {"id": "c1", "name": "Patrick Street Hub", "lat": 51.8995, "lng": -8.4731, "shelter": True, "routes": "205, 208", "transfers": 5},
        {"id": "c2", "name": "UCC Western Road", "lat": 51.8928, "lng": -8.4925, "shelter": True, "routes": "205", "transfers": 3},
        {"id": "c3", "name": "Kent Station Entrance", "lat": 51.9002, "lng": -8.4585, "shelter": False, "routes": "205, 226", "transfers": 2}
    ]
}


@app.get("/")
def read_root():
    return {
        "status": "ok",
        "project": "AimsirGo",
        "team": "Node4",
        "version": "0.1.0",
        "endpoints": ["/weather", "/stops"]
    }


@app.get("/weather")
async def get_weather(
    latitude: float = Query(default=53.2707, description="Latitude (e.g., Galway)"),
    longitude: float = Query(default=-9.0568, description="Longitude (e.g., Galway)"),
):
    """
    Calls Open-Meteo API and returns clean, structured real-time weather metrics.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain", "wind_speed_10m", "weather_code"],
        "timezone": "auto",
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(OPEN_METEO_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Error with Open-Meteo API upstream service: {str(exc)}",
            )

    data = response.json()
    current = data.get("current", {})

    rain_amount = current.get("rain", 0.0)
    is_raining = rain_amount > 0.0

    return {
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": current.get("time"),
        "temperature_celsius": current.get("temperature_2m"),
        "humidity_percent": current.get("relative_humidity_2m"),
        "precipitation_mm": current.get("precipitation", 0.0),
        "rain_mm": rain_amount,
        "is_raining": is_raining,
        "wind_speed_kmh": current.get("wind_speed_10m"),
        "weather_code": current.get("weather_code", 0)
    }


@app.get("/stops")
def get_stops(city: str = Query(default="galway", description="City key: galway, dublin, or cork")):
    """
    Returns regional bus stops annotated with OpenStreetMap shelter tags (`shelter=yes` / `shelter=no`).
    """
    city_key = city.lower()
    if city_key not in MOCK_STOPS_DATA:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found. Available: {list(MOCK_STOPS_DATA.keys())}")
    
    return {
        "city": city_key,
        "count": len(MOCK_STOPS_DATA[city_key]),
        "stops": MOCK_STOPS_DATA[city_key]
    }