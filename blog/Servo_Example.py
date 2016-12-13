#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 300 # Min pulse length out of 4096
servoMax = 200  # Max pulse length out of 4096
'''
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
 pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channe1, 0, pulse)
'''
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(1, 1,servoMin)
  time.sleep(1)
  pwm.setPWM(1, 1, servoMax)
  time.sleep(1)



