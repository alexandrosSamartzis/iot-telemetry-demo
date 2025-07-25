# mqtt_sim/send.py

import pandas as pd
import time
import json
import paho.mqtt.client as mqtt

# --- MQTT Config ---
BROKER = "mqtt-broker"  
PORT = 1883
TOPIC_TEMPLATE = "machine/{machine_id}/metrics"

# --- Load the dataset ---
df = pd.read_csv('data/smart_manufacturing_data.csv') 

# --- MQTT Client setup ---
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# --- Loop through data and send row by row ---
for _, row in df.iterrows():
    machine_id = row["machine_id"]
    topic = TOPIC_TEMPLATE.format(machine_id=machine_id)
    payload = row.to_json()
    
    # Publish the row to its machine-specific topic
    client.publish(topic, payload)
    
    # Optional: Print for debugging
   
    print(f"Sent to {topic}: {payload}")
    
    # Simulate real-time (2 messages per second)
    time.sleep(0.5)

client.disconnect()