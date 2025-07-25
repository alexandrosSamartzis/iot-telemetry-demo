# mqtt_sim/recv.py

import paho.mqtt.client as mqtt
import json
import logging
from datetime import datetime

# --- MQTT Config ---
BROKER = "mqtt-broker"  # docker-compose service name
PORT = 1883
TOPIC_FILTER = "machine/+/metrics"  # '+' matches any machine_id

# === Logging Setup ===
logging.basicConfig(
    filename='logs/recv_messages.log',
    filemode='a',  # Append mode
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# === Print in screen ===
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# --- Callback on connection ---
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_FILTER)

# --- Callback when message is received ---
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    topic = msg.topic
    #print(f"Received from {msg.topic}: {payload}")
    if payload["maintenance_required"] == 1:
        logging.info(f"Received message from topic {msg.topic}: {payload}")
        print(topic)
        print("⚠️⚠️⚠️⚠️  Maintenance needed for Machine", payload["machine_id"])


# --- Setup and start client ---
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()