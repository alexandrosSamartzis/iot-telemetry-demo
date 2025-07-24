# mqtt_sim/recv.py

import paho.mqtt.client as mqtt
import json

# --- MQTT Config ---
BROKER = "mqtt-broker"  # docker-compose service name
PORT = 1883
TOPIC_FILTER = "machine/+/metrics"  # '+' matches any machine_id

# --- Callback on connection ---
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_FILTER)

# --- Callback when message is received ---
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(f"Received from {msg.topic}: {payload}")

# --- Setup and start client ---
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()