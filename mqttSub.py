import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: "+str(rc))

    client.subscribe("ece180d/test/elijah", qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")

def on_message(client, userdata, message):
    #print("Received message: " + str(message.payload) + " on topic '" + message.topic + "' with QoS '" + str(message.qos) + "'")
    #print(message.payload.decode('utf-8'))
    ping = time.time() - float(message.payload)
    print(str(ping) + "s")

client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async("mqtt.eclipseprojects.io")

client.loop_start()

while True:
    pass

client.loop_stop()
client.disconnect()