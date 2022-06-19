from machine import *
import utime

# Servo on p18
d2 = PWM(Pin(18), freq=50, duty=0)

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.duty(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

angel = 0

while True:
  for angel in range(91):
    setServoAngle(d2, angel)
    utime.sleep_ms(1)
    continue
  for angel in range(91, -1, -1):
    setServoAngle(d2, angel)
    utime.sleep_ms(1)