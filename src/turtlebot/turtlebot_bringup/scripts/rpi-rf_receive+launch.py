#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import os

from rpi_rf import RFDevice

rfdevice = None

# Handle exit signal
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

# Argument parser for GPIO pin
parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

# Setup exit handler
signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()

timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))

# Main loop to listen for RF codes
while True:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        logging.info(str(rfdevice.rx_code) +
                     " [pulselength " + str(rfdevice.rx_pulselength) +
                     ", protocol " + str(rfdevice.rx_proto) + "]")
    
    time.sleep(0.01)

    # Trigger TurtleBot to move when an RF code is received
    if rfdevice.rx_code:
        os.system("bash -c 'source /opt/ros/noetic/setup.bash && source /home/SaPHaRI/kobuki_ws/devel/setup.bash && python3 /home/SaPHaRI/kobuki_ws/src/send_goal.py'")

rfdevice.cleanup()
