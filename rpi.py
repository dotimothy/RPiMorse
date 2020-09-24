#author Timothy Do
#RPiMorse: Flashes LED in Morse Code
#Note: Only Works for RPis with GPIO pins. You will be redirected to console version if it doesn't work.

try:
	import RPi.GPIO as GPIO
	import time
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program! Redirecting to console version...\n")
	import morse

#Board Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Set LED pin to pin 11
led = 11
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)





