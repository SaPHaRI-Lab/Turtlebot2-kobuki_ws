#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import os
from rpi_rf import RFDevice

rfdevice = None

# Desired signal parameters
TARGET_CODE = [15205443, 30409795, 23594051, 29361219]
TARGET_PULSELENGTH = [177, 178, 179, 180]
TARGET_PROTOCOL = 1

# Handle exit signal to clean up GPIO
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)

# Set up logging
logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s')

# Argument parser for GPIO pin
parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

# Setup RF device and signal handler
signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))

# Main loop to listen for RF codes
while True:
    if rfdevice.rx_code_timestamp != timestamp:
        timestamp = rfdevice.rx_code_timestamp
        
        # Check if the received code matches the target signal parameters
        if (rfdevice.rx_code in TARGET_CODE and 
            rfdevice.rx_pulselength in TARGET_PULSELENGTH and 
            rfdevice.rx_proto == TARGET_PROTOCOL):
            
            logging.info(f"Target signal received: {rfdevice.rx_code} "
                         f"[pulselength {rfdevice.rx_pulselength}, protocol {rfdevice.rx_proto}]")
            
            # Trigger TurtleBot to move when the target RF code is received
            os.system("bash -c 'source /opt/ros/noetic/setup.bash && "
                      "source /home/SaPHaRI/kobuki_ws/devel/setup.bash && "
                      "python3 /home/SaPHaRI/kobuki_ws/src/send_goal.py'")
        else:
            logging.debug(f"Ignoring unwanted signal: {rfdevice.rx_code} "
                          f"[pulselength {rfdevice.rx_pulselength}, protocol {rfdevice.rx_proto}]")
    
    time.sleep(0.01)

rfdevice.cleanup()
