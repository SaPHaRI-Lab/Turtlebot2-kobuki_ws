#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time, datetime
from collections import deque

# MQTT Config
BROKER = "localhost"
PORT = 1883
TOPICS_SUB = [("esp32/doorbell", 0), ("pi/done", 0), ("pi/unavailable", 0), ("pi/pong", 0)]
# Resource Handling
req_q = deque()                     # to-be-processed queue
pub_q = deque()                     # to-be-published queue
turtlebots = [0, 0, 0, 0, 0, 0]     # turtlebots in use (pi 2 to pi 7, index 0 is pi 2!)
# DEBUG
testing = True  # bypasses time security

def ping_turtlebots():
    for i in range(len(turtlebots)):
        turtlebots[i] = 1
        pub_q.append(('pi/ping', str(i+2), 1))
    print('Updating turtlebots array...')

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code: {reason_code}! \nListening...")
    for topic, qos in TOPICS_SUB:
        client.subscribe(topic, qos=qos)

def on_message(client, userdata, msg):
    print(f'[{datetime.datetime.now()}] Topic: {msg.topic}, Message: {msg.payload.decode()}')
    req_q.append((msg.topic, msg.payload.decode()))

def handle_payload(topic, msg, client):
    if topic == 'esp32/doorbell':
        curr_time = datetime.datetime.now()
        if not testing and not (9 <= curr_time.hour <= 16):
            print('Invalid time. Cannot deploy Turtlebots.')
            return -1
        if sum(turtlebots) == len(turtlebots):
            print('No Turtlebots are available.')
            return -1
        if msg == "test":
            id = 5
        else:
            id = 0
            # Check available turtlebots
            while id < len(turtlebots) and turtlebots[id] != 0:
                id += 1
            id += 2
        turtlebots[id-2] = 1
        print(f'Checks successful. Selecting turtlebot with Pi ID: {id}')
        pub_q.append(('pi/deploy', str(id), 1))     # deploy a turtlebot
        pub_q.append(('esp32/door', 'open', 1))     # deploy a door open
    elif topic == 'pi/done' or topic == 'pi/pong':
        try:
            turtlebots[int(msg)-2] = 0
            print(f'Marked {msg} as free. Turtlebots available: {turtlebots}')
        except Exception as e:
            print(f'Invalid ID given. Exception: {e}')
    elif topic == 'pi/unavailable':
        try:
            turtlebots[int(msg)-2] = 1
            print(f'Marked {msg} as in use or dead. Turtlebots available: {turtlebots}')
        except Exception as e:
            print(f'Invalid ID given. Exception: {e}')

if __name__ == "__main__":
    prevTime = int(time.time())-30
    currTime = int(time.time())
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.on_message = on_message
        client.on_connect = on_connect

        client.connect(BROKER, PORT, 60)
        client.loop_start()

        while True:
            # Check turtlebots' status every 30s
            if currTime - prevTime >= 30:
                ping_turtlebots()
                prevTime = currTime
            # Round Robin lol
            if req_q:
                topic, msg = req_q.popleft()
                handle_payload(topic, msg, client)
            if pub_q:
                topic, msg, qos = pub_q.popleft()
                if topic != 'pi/ping':
                    print(f'Publishing {topic}/{msg} with a QoS of {qos}.')
                client.publish(topic, msg, qos=qos)
    except KeyboardInterrupt as e:
        print("\n\nKeyboard Interrupt, closing...")
        client.loop_stop()