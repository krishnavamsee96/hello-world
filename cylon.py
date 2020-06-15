import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
RPiGPIO = [4,17,18,27]
for pinref in RPiGPIO:
	GPIO.setup(pinref, GPIO.OUT)
StepCounter = 0
StepDir = 1
WaitTime = 0.2
StepCount1 = 4
Seq1 = []
seq1 = list(range(0,StepCount1))
seq1[0] = [1,0,0,0]
seq1[1] = [0,1,0,0]
seq1[2] = [0,0,1,0]
seq1[3] = [0,0,0,1]
StepCount2 = 4
Seq2 = []
Seq2 = list(range(0,StepCount2))
Seq2[0] =[0,0,0,1]
Seq2[1] =[0,0,1,0]
Seq2[2] =[0,1,0,0]
Seq2[3] =[1,0,0,0]
Seq = Seq2
StepCount = StepCount2
while True:
  print("Step: "+ str(StepCounter))
  for pinref in range(0, 4):
    xpin=RPiGPIO[pinref]
    if Seq[StepCounter][pinref]!=0:
      print(" Enable " + str(xpin))
      GPIO.output(xpin, True)
    else:
      print(" Disable " + str(xpin))
      GPIO.output(xpin, False)
  StepCounter += StepDir
  if (StepCounter==StepCount) or (StepCounter<0):
    StepDir = StepDir * -1
    StepCounter = StepCounter + StepDir + StepDir
  time.sleep(WaitTime)
