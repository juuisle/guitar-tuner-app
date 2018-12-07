#!/usr/bin/python
import requests
import serial
import datetime
import os


ROOT_URL = "http://127.0.0.1:5000/selected"

r = requests.get(ROOT_URL)
print r.text

#os.chdir("/home/pi/python")
#ser = serial.Serial("/dev/ttyUSB0",9600)
