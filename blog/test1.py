import sys,tty,termios
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
servoPin=11
servopin=13
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
pwm= GPIO.PWM(servoPin, 50)
pwm2= GPIO.PWM(13, 50)
pwm3= GPIO.PWM(15, 50)
pwm.start(2)
pwm2.start(10)
pwm3.start(7)
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):


                k=inkey()
                if k!='':break
              
        if k=='\x1bOQ':
                print "F2"
               
                for i in range(1, 2):
                    print "Enter Angle Between ( 20 - 70)"

                    desiredPosition=input("Enter Angle: ")
                    print "Enter Angle Between ( 120 - 150)"
                    desiredPosition1=input("Enter Angle: ")
                    DC= 1./18.*(desiredPosition)+2
                    pwm.ChangeDutyCycle(DC)
                    time.sleep(0.03)
                    
                    DC2= 1./18.*(desiredPosition1)+2
                    pwm2.ChangeDutyCycle(DC2)
                    time.sleep(0.03)
                    print "->>  Prass F2 to continue..."
                    print "->>  Prass F3 Clamp it and Released "
                    print "->>  Prass F4 Reset Robot "
                    print "->>  Prass to Start: 
               
                    
                    
        elif k=='\x1bOR':
                print "F3"
                print "open = 80"
                print "close = 130"
                
                for i in range(1, 2):
                    
                    desiredPosition3=input("Enter Angle: ")
                    DC3= 1./18.*(desiredPosition3)+2
                    pwm3.ChangeDutyCycle(DC3)
                    time.sleep(0.03)
                    print "->>  Prass F2 to continue..."
                    print "->>  Prass F3 Clamp it and Released "
                    print "->>  Prass F4 Reset Robot "
                    print "->>  Prass to Start: 
        elif k=='\x1b[15':
                print "F4"
                print "Robot Has been Reset it"
                pwm.start(2)
                pwm2.start(10)
                pwm3.start(7)

        elif k=='\x1bOS':
                print "F5"
                sys.exit()
        
        else:
                print "not an arrow key!"
                pwm.stop()
                pwm2.stop()
                GPIO.cleanup()

def main():
        print "->>  Prass F2 to movie up and down"
        print "->>  Prass F3 Clamp it and Released "
        print "->>  Prass F4 Reset Robot "
        print "->>  Prass to Start: "
        while 1:
        #for i in range(0,20):
                get()

if __name__=='__main__':
        main()
