try:
	import RPi.GPIO as GPIO
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program!"),
	exit()
	
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)


while True:
	GPIO.output(11,True)
	print("LED On")
	time.sleep(.5)
	GPIO.output(11, False)
	print("LED Off")
	time.sleep(.5)
GPIO.cleanup()
