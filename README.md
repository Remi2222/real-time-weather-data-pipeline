#  Real-Time Weather Data Pipeline with Airflow, dbt, PostgreSQL & Superset

## Overview

This project demonstrates an end-to-end data engineering pipeline that automates the ingestion, transformation, and visualization of real-time weather data.

Weather data is collected from the **OpenWeatherMap API**, stored in **PostgreSQL**, transformed with **dbt**, orchestrated by **Apache Airflow**, and visualized through **Apache Superset**. The entire infrastructure is containerized using **Docker Compose** for easy deployment and reproducibility.

---

##  Tech Stack

- Python
- OpenWeatherMap API
- PostgreSQL
- Apache Airflow
- dbt (Data Build Tool)
- Apache Superset
- Docker & Docker Compose

---

##  Architecture

<p align="center">
  <img src="images/Project Architecture.PNG" alt="Pipeline Architecture" width="900">
</p>

### Data Flow

```
OpenWeatherMap API
        │
        ▼
Python Extraction Script
        │
        ▼
PostgreSQL (Raw Layer)
        │
        ▼
dbt Transformations
        │
        ▼
Analytics Tables
        │
        ▼
Apache Superset Dashboard
```

Airflow orchestrates the complete workflow by executing the ingestion script followed by the dbt transformations.

---

##  Project Structure

```text
.
├── airflow/
│   └── dags/
│       └── orchestrator.py
│
├── scripts/
│   ├── api_request.py
│   └── insert_records.py
│
├── dbt/
│   ├── my_project/
│   │   ├── models/
│   │   │   ├── source/
│   │   │   ├── staging/
│   │   │   └── mart/
│   │   ├── dbt_project.yml
│   │   └── profiles.yml
│
├── postgres/
│
├── docker/
│
├── docker-compose.yml
│
└── README.md
```

---

##  Features

- Extract real-time weather data from OpenWeatherMap API
- Store raw data in PostgreSQL
- Automatically create the database schema
- Transform raw data using dbt models
- Orchestrate the pipeline with Apache Airflow
- Visualize transformed data using Apache Superset
- Fully containerized with Docker Compose

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Real-Time-Weather-Data-Pipeline.git
cd Real-Time-Weather-Data-Pipeline
```

### 2. Configure environment variables

Create a `.env` file:

```env
WEATHER_API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

### 3. Start the services

```bash
docker compose up -d
```

---

##  Access the Applications

| Service | URL |
|----------|-----|
| Airflow | http://localhost:8000 |
| Superset | http://localhost:8088 |
| PostgreSQL | localhost:5403 |

---

##  Pipeline Execution

1. Airflow triggers the ingestion task.
2. Weather data is fetched from the OpenWeatherMap API.
3. Raw data is inserted into PostgreSQL.
4. dbt transforms the raw tables into analytics-ready models.
5. Superset connects to PostgreSQL and visualizes the transformed data.

---



---

## Environment Variables

| Variable | Description |
|----------|-------------|
| WEATHER_API_KEY | OpenWeatherMap API Key |



## Author

**Maryam Fajri**

- LinkedIn: https://www.linkedin.com/in/maryam-fajri/
- GitHub: https://github.com/YOUR_USERNAME