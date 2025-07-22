
# Smart Manufacturing IoT Monitoring – DevOps & Edge Analytics (Learning Project)

This project explores an IoT-data pipeline using real-time sensor data from a synthetic smart manufacturing environment. It is developed as a personal learning exercise to better understand how edge data is ingested, processed, and visualized—focusing on DevOps principles, basic telemetry parsing, and system monitoring.

## 📍 Purpose

The goal is to simulate a simplified predictive maintenance workflow using open IoT data. While the dataset includes machine learning labels, this project currently **excludes model training** and instead emphasizes:

- Local data ingestion
- Sensor sanity checks and visualization
- MQTT-based message streaming
- Lightweight dashboarding
- Docker-based microservice deployment (FastAPI)

## 🔧 Dataset Overview

Source: [Smart Manufacturing IoT-Cloud Monitoring Dataset (Kaggle)] 
(https://www.kaggle.com/datasets/ziya07/smart-manufacturing-iot-cloud-monitoring-dataset)

- 100,000 time-series sensor records from 50 machines
- Readings include: temperature, vibration, humidity, pressure, and energy
- Timestamps at 1-minute intervals
- Flags for anomalies and machine failures
- Target column: `maintenance_required` (0 or 1)

This dataset is well-suited for building predictive maintenance pipelines, real-time dashboards, and cloud-based IoT systems.

## 🔍 Planned Project Milestones

| Phase                 | Deliverables                                |
|----------------------|---------------------------------------------|
| ✅ Environment Setup  | Conda/Docker environment + GitHub repo      |
| ⬜ EDA                | Basic plots, null checks, class balance     |
| ⬜ MQTT Simulation    | Row-by-row publisher / subscriber pair      |
| ⬜ Monitoring UI      | Grafana Cloud panel or Streamlit frontend   |
| ⬜ FastAPI Service    | Containerized model or rule-based alert API |
| ⬜ Architecture Notes | Short .md and system diagram                |

## 🚧 Status

Day 1: Initial environment and repo structure complete. Exploratory analysis in progress.

## ⚠️ Disclaimer

This project is for educational and personal development purposes only. It is not affiliated with any company or official production use case.