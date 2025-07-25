
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
- Target column for ML if needed: `maintenance_required` (0 or 1)

-- Further Details

-- Machine Status – Indicates whether the machine is Idle, Running, or in Failure
-- Anomaly Flags – Identifies extreme values in temperature and vibration
-- Predicted Remaining Life – Estimated time before maintenance is needed
-- Failure Type – The reason for machine failure (e.g., Overheating, Vibration Issue)
-- Downtime Risk Score – Probability of machine breakdown


This dataset is well-suited for building predictive maintenance pipelines, real-time dashboards, and cloud-based IoT systems.

## 🔍 Planned Project Milestones

| Phase                 | Deliverables                                |
|----------------------|---------------------------------------------|
| ✅ Environment Setup  | Conda/Docker environment + GitHub repo      |
| ✅ EDA                | Basic plots, null checks, class balance     |
| ✅ MQTT Simulation    | Row-by-row publisher / subscriber pair      |
| ⬜ Monitoring UI      | Grafana Cloud panel or Streamlit frontend   |
| ⬜ FastAPI Service    | Containerized model or rule-based alert API |
| ⬜ Architecture Notes | Short .md and system diagram                |

## 🚧 Launch

1. Build Docker Images             ---->  docker compose build
This step builds both:
	•	The Python App container (send + receive)
	•	The Mosquitto MQTT broker
2. Launch the Containers           ----> docker compose up
   	•	Starts two containers: the app and the broker
	•	Mounts necessary configs and ports
	•	Connects them via a shared network
3. Access the Running Containers   ----> docker exec -it iot-devops-app bash
    (if you want to coinfirm the existance of images ---> docker ps)
4. run the send data and recv data ----> python mqtt_sim/send.py
                                   ----> python mqtt_sim/recv.py



## ⚠️ Disclaimer

This project is for educational and personal development purposes only. It is not affiliated with any company or official production use case.