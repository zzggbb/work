#!/bin/python3

import serial

DEVPORT = '/dev/tty.usbmodem1421'
RATE=9600

s = serial.Serial(port=DEVPORT,baudrate=RATE)

def parse(cmd):
	if 'blink' in cmd:
		return cmd[:5]*(int(cmd[5:]))
	return cmd

while (True):
	text = list(map(parse,input("Type a command: ").split(" ")))
	print(text)
	"""
	for command in text:
		s.write((command + '\n').encode())
	"""
s.close()
