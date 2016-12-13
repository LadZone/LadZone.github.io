import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin=11
servopin=13
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwm= GPIO.PWM(servoPin, 50)
pwm2= GPIO.PWM(13, 50)
pwm.start(2)
pwm2.start(10)
for i in range(0, 20):
	desiredPosition=input("left 0-180: ")
	
	DC= 1./18.*(desiredPosition)+2
	pwm.ChangeDutyCycle(DC)
	time.sleep(0.03)
	desiredPosition1=input("Right? 0-180: ")
	DC2= 1./18.*(desiredPosition1)+2
	pwm2.ChangeDutyCycle(DC2)
	time.sleep(0.03)
pwm.stop()
pwm2.stop()
GPIO.cleanup()
