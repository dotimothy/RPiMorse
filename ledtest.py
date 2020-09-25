try:
	import RPi.GPIO as GPIO
except ModuleNotFoundError: 
	print("You don't have GPIO Pins, so you can't run this program!"),
	exit()
	
import time

led = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)


while True:
	print("LED On")
	GPIO.output(11,True)
	time.sleep(1)
	print("LED Off")
	GPIO.output(11, False)
	time.sleep(1)
GPIO.cleanup()
