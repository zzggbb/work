#!/usr/local/bin/python3
import serial
from firebase import firebase
import time

APP='https://arduinobt.firebaseio.com'
PORT='/dev/tty.HC-06-DevB'
RATE=9600

f = firebase.FirebaseApplication(APP,None)
s = serial.Serial(port=PORT, baudrate=RATE)

while True:
	try:
		web_value = str(f.get('/light-value',None))
		print (web_value)
		s.write(str(web_value).encode())
		time.sleep(0.5)

	except (KeyboardInterrupt, EOFError):
		print()
		print("Closing serial...")
		s.close()
		break
		print()