#/usr/bin/env python3

from gpiozero import LED, Button
from time import sleep

NULL_CHAR = chr(0)

def write_report(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

def write_byte_array(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report)

unmute_array = bytearray([0x04,0,0x04,0,0,0,0,0])


mod = str(0b00000111) + "\0\0\0\0\0\0\0" # Defines the control bytes for CTRL + SHIFT + ALT plus seven bytes?? for a full message

off = "\0\0\0\0\0\0\0\0"

unmute = str(0b00000100) + NULL_CHAR + chr(4) + NULL_CHAR*5

led = LED(4)
button = Button(23)

light_state = False

while True:
	button.wait_for_press() # wait for a button press
	if not light_state:
		led.on()
		light_state = True
	else:
		led.off()
		light_state = False
	print(mod)
	write_report(mod)
	sleep(.2)
	write_report(off)
	sleep(.2)
	print(unmute)
	write_byte_array(unmute_array) # for some reason, this wouldn't work without a bytearray for unknown reasons
	sleep(.2)
	write_report(off)
