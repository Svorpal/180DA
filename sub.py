# reference: https://github.com/michellektan/180DA-WarmUp/blob/main/Tutorial2-Comms/MQTT/test_client.py

import paho.mqtt.client as mqtt
import random

port = 1883
topic = "ece180d/test"
client_id = f'python-mqtt-{random.randint(0,100)}'
broker = 'broker.emqx.io'

def connect_mqtt() -> mqtt:
	def on_connect(client, userdata, flags, rc):
		if rc != 0:
			print("Failed to connect, return code %d\n", rc)
		else:
			print("Connected to MQTT Broker!")

	client = mqtt.Client(client_id)
	client.on_connect = on_connect
	client.connect(broker, port)
	return client

def subscribe(client: mqtt):
	def on_message(client, userdata, msg):
		print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

	client.subscribe(topic)
	client.on_message = on_message

def run():
	client = connect_mqtt()
	subscribe(client)
	client.loop_forever()

if __name__ == '__main__':
	run()