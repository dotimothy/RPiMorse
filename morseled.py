try:
	import RPi.GPIO as GPIO
	import time
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program! Redirecting to console version...")
	import morse

#Board Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Set LED pin to pin 11
led = 11
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)



