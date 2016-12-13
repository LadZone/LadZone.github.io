import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
servoPin=11
GPIO.setup(servoPin, GPIO.OUT)
pwm= GPIO.PWM(servoPin, 50)
pwm.start(7)
#for i in range(0, 20):

	#DC= 1./18.*(desiredPosition)+2
	#pwm.ChangeDutyCycle(DC)

#def move (servoPin, pwm):
import getch
while True:
    key = ord(getch())
    if key == 80:
          for i in range(0, 180):
	    DC= 1./18.*(i)+2
	    pwm.ChangeDutyCycle(DC)
	    time.sleep(0.01)
    if key == 72:
          for i in range(180,0,-1):
	    DC=1/18.*i+2
	    pwm.ChangeDutyCycle(DC)
	    time.sleep(0.01)

	    
#desiredPosition=input("where do you want the servo? 0-180: ")
#if desiredPositionser == '1':
    #for i in range(0, 180):
	   # DC= 1./18.*(i)+2
	    #pwm.ChangeDutyCycle(DC)
	   # time.sleep(0.01)
#elif servoPin == '2':
    #for i in range(180,0,-1):
	    #DC=1/18.*i+2
	   # pwm.ChangeDutyCycle(DC)
	   # time.sleep(0.01)
        
pwm.stop()
GPIO.cleanuo()
