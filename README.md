# AimsirGo 🌦️🚌

> **A real-time, weather-resilient transit routing engine for Irish commuters.**  
> Developed by **Node4** as part of the Software Engineering module (Year 2, Computer Science & IT).

---

## 📌 Overview

In Ireland, transit navigation apps often optimize strictly for the shortest arrival time, frequently sending commuters on long, unsheltered walks during heavy rain or wind warnings.

**AimsirGo** solves this by factoring live weather conditions and public shelter data into route planning. The application dynamically adjusts travel routes and transfer recommendations to minimize rain exposure and avoid unshielded stops during severe weather conditions.

---

## 📊 Timeline Summary

| Phase | Timeline | Focus Area | Key Deliverables |
| :--- | :--- | :--- | :--- |
| **Phase 1** | October 2026 | Environment & Weather Ingestion | Git setup, FastAPI `/weather` endpoint, Leaflet interactive canvas |
| **Phase 2** | November 2026 | Shelter Geodata Extraction | OSM Overpass dataset, `/stops` API, custom shelter map pins |
| **Phase 3** | **December 2026** | **Live Assessment & Demo** | **Resilient MVP showcase, offline failover mode, live walkthrough** |
| **Phase 4** | January 2027 | Spatio-Temporal Routing | Checkpoint-based precipitation evaluation, Rain Exposure Index |
| **Phase 5** | February 2027 | Live Transit Feeds (NTA) | GTFS-RT delay parsing, dynamic delay warnings at exposed stops |
| **Phase 6** | March 2027 | Alert Worker & Testing | Discord commute alerts, `pytest`, GitHub Actions CI |
| **Phase 7** | April 2027 | Cloud Deployment & Final Defense | GCP Cloud Run backend, Vercel frontend, final viva/presentation |
---

## 👥 The Team: Node4

* **Team Name:** Node4 
* **Frontend Sub-team:** Interactive Leaflet map, responsive UI/UX, visualization.
* **Backend & Data Sub-team:** FastAPI service, Open-Meteo ingestion, Overpass/OSM stop shelter parsing, routing logic.

---

## 🏗️ Architecture & Tech Stack

* **Frontend:** React, Leaflet (`react-leaflet`), Tailwind CSS
* **Backend:** Python, FastAPI, Uvicorn, Requests / HTTPX
* **Data Sources (Open Data APIs):**
  * **Weather:** [Open-Meteo API](https://open-meteo.com/) (Live rain/wind conditions & 15-minute forecasts)
  * **Shelter & Stops:** [OpenStreetMap (Overpass API)](https://overpass-turbo.eu/) for bus shelter metadata (`shelter=yes/no`)
  * **Transit (Future):** Transport for Ireland (TFI) / National Transport Authority (NTA) GTFS feeds

---

## 📂 Project Structure
aimsir-go/
├── README.md               # Project documentation and roadmap
├── LICENSE                 # MIT License
├── .gitignore              # Ignored files (node_modules, .venv, etc.)
│
├── backend/                # Python (FastAPI) backend service
│   ├── app/
│   │   ├── main.py         # Entry point for the FastAPI server
│   │   ├── routers/        # API route handlers (/weather, /stops)
│   │   └── services/       # Weather & OSM data parsing services
│   ├── data/               # Static datasets (e.g. Galway bus stops GeoJSON)
│   └── requirements.txt    # Python dependencies
│
└── frontend/               # React + Tailwind CSS client
    ├── src/
    │   ├── components/     # UI elements (Map.jsx, WeatherWidget.jsx)
    │   └── App.jsx         # Main application component
    └── package.json        # Node dependencies & scripts
