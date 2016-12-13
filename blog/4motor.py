#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from Adafruit_PWM_Servo_Driver import PWM

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout

PWMOUT = 0
PWMOUT2 = 1 #left M
PWMOUT3 = 2 #left/right
PWMOUT4 = 3  #right M

SPICLK = 22
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the interface pins
#GPIO.setup(PWMOUT, GPIO.OUT)
#GPIO.setup(PWMOUT2, GPIO.OUT)


#GPIO.setup(PWMOUT3, GPIO.OUT)
#GPIO.setup(PWMOUT4, GPIO.OUT)

GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# 10k trim pot connected to adc #0
ch1 =0;
ch2 = 1;

ch3 =2;
ch4 = 3;     # Set the PWM frequency to 50 Hz
last_read = 0       # this keeps track of the last potentiometer value
tolerance = 1      # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'

# Configure the PWM pin
#p = GPIO.PWM(PWMOUT, pwm_freq)  # channel=18 frequency=50Hz
#p2 = GPIO.PWM(PWMOUT2, pwm_freq) #channel =17 frequency=50Hz

#p3 = GPIO.PWM(PWMOUT3, pwm_freq)  # channel=18 frequency=50Hz
#p4 = GPIO.PWM(PWMOUT4, pwm_freq) #channel =17 frequency=50Hz
p1 =pwm.setPWMFreq(30)
p2 =pwm.setPWMFreq(30)
p3 =pwm.setPWMFreq(30)
p4 =pwm.setPWMFreq(30) 

#p3.start(0)

#p4.start(0)

#p2.start(9)

#p.start(1)

try:
  while True:
    # we'll assume that the pot didn't move
    trim_pot_changed = False
    trim_pot_changed2 = False

    trim_pot_changed3 = False
    trim_pot_changed4 = False


    # read the analog pin
    trim_pot = readadc(ch1, SPICLK, SPIMOSI, SPIMISO, SPICS)

    trim_pot2 = readadc(ch2, SPICLK, SPIMOSI, SPIMISO, SPICS)

    trim_pot3 = readadc(ch3, SPICLK, SPIMOSI, SPIMISO, SPICS)

    trim_pot4 = readadc(ch4, SPICLK, SPIMOSI, SPIMISO, SPICS)

    
    # how much has it changed since the last read?
    pot_adjust = abs(trim_pot - last_read)
    pot_adjust2 = abs(trim_pot2 - last_read)
    pot_adjust3 = abs(trim_pot3 - last_read)
    pot_adjust4 = abs(trim_pot4 - last_read)

    if ( pot_adjust > tolerance ):
        trim_pot_changed = True
        last_read = trim_pot


    elif ( pot_adjust2 > tolerance ):
        trim_pot_changed2 = True
        last_read = trim_pot2




        
    elif ( pot_adjust3 > tolerance ):
        trim_pot_changed3 = True
        last_read = trim_pot3


    elif ( pot_adjust4 > tolerance ):
        trim_pot_changed4 = True
        last_read = trim_pot4




     

    if ( trim_pot_changed ):
        pwm_pct = round(trim_pot)  # Determine current voltage percentage
        pwm_pct = int(pwm_pct)            # Cast the value as an integer
        #DC= 1./18*(pwm_pct)
        print "Ch1:"
        print "ADC read: ", trim_pot
        print "PWM percentage: ", pwm_pct
        #print "PWM Duty Cycle: ", DC 
        pwm.setPWM(PWMOUT, 4,pwm_pct)
        #p.ChangeDutyCycle(DC)
        #time.sleep(0.01)


    elif ( trim_pot_changed2 ):
        pwm_pct2 = round(trim_pot2)  # Determine current voltage percentage
        pwm_pct2 = int(pwm_pct2)-100            # Cast the value as an integer
        #DC= 1./18*(pwm_pct)
        print "Ch2:"
        print "ADC read: ", trim_pot2
        print "PWM percentage: ", pwm_pct2
        #print "PWM Duty Cycle: ", DC 
        pwm.setPWM(PWMOUT2, 4,pwm_pct2)
        #p.ChangeDutyCycle(DC)
        time.sleep(0.01)



    if ( trim_pot_changed3 ):
        pwm_pct3 = round(trim_pot3)  # Determine current voltage percentage
        pwm_pct3 = int(pwm_pct3)            # Cast the value as an integer
        #DC= 1./18*(pwm_pct)
        print "Ch3:"
        print "ADC read: ", trim_pot3
        print "PWM percentage: ", pwm_pct3
        #print "PWM Duty Cycle: ", DC 
        pwm.setPWM(PWMOUT3, 1,pwm_pct3)
        #p.ChangeDutyCycle(DC)
        time.sleep(0.01)


    elif ( trim_pot_changed4 ):
        pwm_pct4 = round(trim_pot4)  # Determine current voltage percentage
        pwm_pct4 = int(pwm_pct4)-100            # Cast the value as an integer
        #DC= 1./18*(pwm_pct)
        print "Ch4:"
        print "ADC read: ", trim_pot4
        print "PWM percentage: ", pwm_pct4
        #print "PWM Duty Cycle: ", DC 
        pwm.setPWM(PWMOUT4, 1,pwm_pct4)
        #p.ChangeDutyCycle(DC)
        time.sleep(0.01)
   
    '''
    if ( trim_pot_changed3 ):
        pwm_pct3 = round(trim_pot3)  # Determine current voltage percentage
        pwm_pct3 = int(pwm_pct3)-150           # Cast the value as an integer
        #DC3= 1./18*(pwm_pct3)
        print "Ch3:"
        print "ADC read: ", trim_pot3
        print "PWM percentage: ", pwm_pct3
        #print "PWM Duty Cycle: ", DC3
        pwm.setPWM(PWMOUT3, 1,pwm_pct3)
        
        #p3.ChangeDutyCycle(DC3)
        #time.sleep(0.01)



    elif ( trim_pot_changed4 ):
        pwm_pct4 = round(trim_pot4) # Determine current voltage percentage
        pwm_pct4 = int(pwm_pct4)          # Cast the value as an integer
       # DC4= 1./18*(pwm_pct4)
        print "Ch4:"
        print "ADC read: ", trim_pot4
        print "PWM percentage: ", pwm_pct4
        #print "PWM Duty Cycle: ", DC4 
        pwm.setPWM(PWMOUT4, 1,pwm_pct4)
        #p4.ChangeDutyCycle(DC4)
        #time.sleep(0.1)
    '''
    # hang out and do nothing for a half second
    time.sleep(0.5)
except KeyboardInterrupt:
    pass

p1.stop()
p2.stop()
p3.stop()
p4.stop()
GPIO.cleanup()
