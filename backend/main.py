from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(
    title="AimsirGo API",
    description="Weather resilient transit routing backend",
    version="0.1.0",
)

# permission CORS, so React frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


@app.get("/")
def read_root():
    return {"status": "ok", "project": "AimsirGo", "team": "Node4"}


@app.get("/weather")
async def get_weather(
    latitude: float = Query(default=53.2707, description="Latitude (e.g., Galway)"),
    longitude: float = Query(default=-9.0568, description="Longitude (e.g., Galway)"),
):
#calls Open-Meteo API and returns clear weather data in real time
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "precipitation", "rain", "wind_speed_10m"],
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(OPEN_METEO_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Error with Open-Meteo API: {str(exc)}",
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
        "rain_mm": rain_amount,
        "is_raining": is_raining,
        "wind_speed_kmh": current.get("wind_speed_10m"),
    }
