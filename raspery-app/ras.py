#!/usr/bin/python
import requests
import serial
import datetime
import os
import time
ser = serial.Serial(
    port='/dev/ttyAMC0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
#last_one = 
ROOT_URL = "http://127.0.0.1:5000/selected"
#ser.open()
while(1):
	r = requests.get(ROOT_URL)
	print (r.text)
	if (last_one.text != r.text):
		ret = ser.write('1=' + r.text.str_one + '|' + '2=' + r.text.str_two + '|' +
		'3=' + r.text.str_three + '|' +'4=' + r.text.str_four + '|' + 
		'5=' + r.text.str_five + '|' +'6=' + r.text.str_six +'!\r\n')
		time.sleep(1)
		if (ret > 0):
			last_one = r.text
		
	

ser.close()
#os.chdir("/home/pi/python")
