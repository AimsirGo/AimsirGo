# AimsirGo — Development Roadmap (Academic Year 2026/2027)

## 🍁 Semester 1: Foundations & Resilient MVP (Oct 2026 – Dec 2026)
*Target: Deliver a fully functional, fault-tolerant client-server prototype featuring live weather integration and shelter-annotated stops for the December Live Assessment.*

### Month 1: October 2026 — Foundations & Live Data Ingestion
* **Team Operations:**
  * Configure organization repository, branch protection rules, and GitHub Projects board.
  * Establish weekly sync sprints and code review conventions.
* **Backend Sub-Team (FastAPI):**
  * Initialize Python application structure and dependency tracking (`requirements.txt`).
  * Integrate Open-Meteo API to consume live precipitation, temperature, and wind speed parameters.
  * Expose first operational endpoint: `GET /weather` returning structured JSON metrics.
* **Frontend Sub-Team (React + Leaflet):**
  * Scaffold client application with Vite and Tailwind CSS.
  * Integrate `react-leaflet` to render interactive base map centered on the campus/city region.
  * Connect to client network layer to test cross-origin communication with backend.
* 🎯 **Milestone (End of Oct):** Live weather endpoint verified; frontend map rendered.

### Month 2: November 2026 — Shelter Geodata Extraction & System Integration
* **Backend Sub-Team (FastAPI):**
  * Query OpenStreetMap bus stops with `shelter=yes` / `shelter=no` tags using Overpass Turbo.
  * Clean, serialize, and store regional stop data (`backend/data/stops.json`).
  * Implement `GET /stops` endpoint with bounding-box parameter filtering.
* **Frontend Sub-Team (React + Leaflet):**
  * Ingest `/stops` payload and plot customized map markers:
    * ☂️ **Covered Stops:** Distinct marker style for `shelter=yes`.
    * ⚠️ **Exposed Stops:** Neutral marker style for `shelter=no` or unspecified shelter tags.
  * Implement real-time weather HUD widget displaying current rain intensity and conditions.
* 🎯 **Milestone (End of Nov):** Interactive map overlay displaying live weather alongside shelter-annotated transit stops. **Enforce Feature Freeze for Semester 1.**

### Month 3: December 2026 — Live Assessment & Demo Readiness
* **Full Team (Hardening & Assessment Preparation):**
  * **System Hardening:** Strict feature freeze; resolve edge cases and eliminate unhandled API exceptions.
  * **Offline Mock & Failover Mode:** Embed local JSON fallback fixtures for both weather and stop datasets to protect against classroom Wi-Fi instability or third-party API downtime during evaluation.
  * **Curated Route Scenarios:** Select verified campus/urban walking corridors demonstrating contrast:
    * *Scenario A (Rain Event):* Routing engine prioritizes sheltered stop transfers.
    * *Scenario B (Clear Weather):* Routing engine defaults to direct, fastest pedestrian walk.
  * **Presentation Walkthrough:** Prepare technical demonstration slide deck and conduct dry runs.
* 🎯 **Semester 1 Final Milestone:** Flawless live demonstration to university examiners; functional MVP successfully evaluated.

---

## 🌸 Semester 2: Algorithmic Routing, Live Transit & Cloud Deployment (Jan 2027 – Apr 2027)
*Target: Introduce advanced spatio-temporal path heuristics, live GTFS-RT delay updates, automated alerting workers, and production cloud infrastructure.*

### Month 4: January 2027 — Spatio-Temporal Route Evaluation
* **Backend Sub-Team:**
  * Implement multi-checkpoint route evaluation: split journeys into discrete legs and forecast arrival timestamps.
  * Query short-interval forecast data (`minutely_15` via Open-Meteo) for expected conditions upon arrival at transfer stops.
  * Formulate initial "Rain Exposure Index" combining walking duration and precipitation intensity.
* **Frontend Sub-Team:**
  * Render route polylines color-coded by exposure risk (e.g., sheltered vs. exposed segments).
  * Build user origin/destination search fields and interactive pin selection.

### Month 5: February 2027 — Real-Time Transit Feeds (NTA GTFS-RT)
* **Backend Sub-Team:**
  * Ingest National Transport Authority (NTA / Transport for Ireland) GTFS static schedules and GTFS-Realtime vehicle delay streams.
  * Link dynamic delay alerts to stop conditions: flag long transfer delays occurring at unsheltered stops during rain.
* **Frontend Sub-Team:**
  * Render transit line badges with real-time delay chips (e.g., `Route 401: +8 min delay — Heavy Rain Alert`).
  * Ensure full responsive UI/UX across mobile devices and tablet viewports.

### Month 6: March 2027 — Alerting Automation & CI/CD Pipelines
* **DevOps & Notifications:**
  * Implement lightweight Telegram/Discord notification bot providing scheduled commute summaries.
  * Set up automated test suite using `pytest` to validate core routing logic and fallback handlers.
  * Configure GitHub Actions CI pipeline executing automated test suites on every Pull Request.

### Month 7: April 2027 — Cloud Deployment, Polish & Final Defense
* **Deployment (Google Cloud Platform & Web):**
  * Containerize the FastAPI backend via Docker.
  * Deploy backend service to **Google Cloud Platform (Cloud Run)** utilizing academic Google Cloud credits.
  * Deploy production React frontend to Vercel/Netlify.
* **Documentation & Final Delivery:**
  * Complete root `README.md` with system architecture diagrams, live demo URLs, and benchmark documentation.
  * Deliver final capstone presentation and technical defense.
* 🎯 **Semester 2 Final Milestone:** Production-ready web platform deployed to the cloud, public live URL, and exceptional engineering portfolio artifact.
