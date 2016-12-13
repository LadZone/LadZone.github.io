#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)  # channel=18 frequency=50Hz
p.start(0)
try:
    while 1:
        for i in range(0, 180):
		DC= 1./18.*(i)+2
		p.ChangeDutyCycle(DC)
		time.sleep(0.05)
	for i in range(180,0,-1):
		DC=1/18.*i+2
		p.ChangeDutyCycle(DC)
		time.sleep(0.05)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
