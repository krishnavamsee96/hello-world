import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
button1 = 11
button2 = 13
button3 = 15
LED1 = 12
LED2 = 16
LED3 = 18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
BS1 = False
BS2 = False
BS3 = False
while(1):
	if GPIO.input(button1)==0:
		print('Button1 is pressed')
		if BS1==False:
			GPIO.output(LED1,True)
			BS1 = True
			time.sleep(0.5)
		else:
			GPIO.output(LED1,False)
			BS1 = False
			time.sleep(0.5)
	if GPIO.input(button2)==0:
		print('Button2 is pressed')
		if BS2==False:
			GPIO.output(LED2,True)
			BS2 = True
			time.sleep(0.5)
		else:
			GPIO.output(LED2,False)
			BS2 = False
			time.sleep(0.5)
	if GPIO.input(button3)==0:
		print('Button3 is pressed')
		if BS3==False:
			GPIO.output(LED3,True)
			BS3 = True
			time.sleep(0.5)
		else:
			GPIO.output(LED3,False)
			BS3 = False
			time.sleep(0.5)
GPIO.cleanup()
	
