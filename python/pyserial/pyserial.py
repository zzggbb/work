#!/bin/python3

import serial
import glob

PORT = glob.glob("/dev/tty.usb*")[0]
RATE=9600
CMDS = ['on','off','pause']

s = serial.Serial(port=PORT,baudrate=RATE)

while (True):
	raw = input("Type a command: ").split(" ")
	ok = list(filter(lambda x: x in CMDS, raw))
	bad = list(set(raw) - set(ok))
	if bad: print ("These commands aren't valid: " + " ".join(bad))
	for command in ok:
		s.write((command + '\n').encode())
s.close()
