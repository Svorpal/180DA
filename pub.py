# reference: https://github.com/michellektan/180DA-WarmUp/blob/main/Tutorial2-Comms/MQTT/test_client.py

import paho.mqtt.client as mqtt
import numpy as np
import random
import time

port = 1883
topic = "ece180d/test"
client_id = f'python-mqtt-{random.randint(0,1000)}'
broker = 'broker.emqx.io'


def connect_mqtt():
	def on_connect(client, userdata, flags, rc):
		if rc != 0:
			print("Failed to connect, return code %d\n", rc)
		else:
			print("Connected to MQTT Broker!")
	# set connecting client ID
	client = mqtt.Client(client_id)
	client.on_connect = on_connect
	client.connect(broker, port)
	return client

def publish(client):
	msg_count = 0
	while True:
		time.sleep(1.5)
		msg = f"messages: {msg_count}"
		result = client.publish(topic,msg)
		# result: [0,1]
		status = result[0]
		if status == 0:
			print(f"Send '{msg}' to topic '{topic}'")
		else:
			print(f"Failed to send message to topic {topic}")
		msg_count += 1

def run():
	client = connect_mqtt()
	client.loop_start()
	publish(client)

if __name__ == '__main__':
	run()