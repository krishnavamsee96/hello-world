import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = GPIO.PWM(12,50)
p.start(7.5)
try:
	while True:
		input_state = GPIO.input(26)
		if input_state == False:
			p.ChangeDutyCycle(2.5)
		input_state = GPIO.input(24)
		if input_state == False:
			p.ChangeDutyCycle(12.5)
		input_state = GPIO.input(24) and GPIO.input(26)
		if input_state == False:
			p.ChangeDutyCycle(7.5)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
