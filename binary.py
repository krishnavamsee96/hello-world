import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
c = 0
try:
	while True:
		c = (c+1) % 8
		GPIO.output(11, (c >> 0) & 1)
		GPIO.output(13, (c >> 1) & 1)
		GPIO.output(15, (c >> 2) & 1)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
