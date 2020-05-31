import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
print('Enter below numbers to on different LEDs')
print('1.RED')
print('2.WHITE')
print('3.GREEN')
print('4.ALL')
n = int(input('Enter a number:'))
if n == 1:
	GPIO.output(11,GPIO.HIGH)
	time.sleep(5)
	print('Red LED is on')
	GPIO.output(11,GPIO.LOW)
elif n==2:
	GPIO.output(13,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(13,GPIO.LOW)
	print('White LED is on')
elif n==3:
	GPIO.output(15,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(15,GPIO.LOW)
	print('Green LED is on')
elif n==4:
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
elif n>4:
	print('Wrong selection')
GPIO.cleanup()
