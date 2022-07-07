from machine import Pin, PWM
import time

SERVO_PIN = 18
servo = PWM(Pin(SERVO_PIN), freq=50)

def rotate():
    servo.duty(30)
    time.sleep(1)
    servo.duty(40)
    time.sleep(1)
    servo.duty(50)
    time.sleep(1)
    servo.duty(90)
    time.sleep(1)

    servo.duty(30)
    time.sleep(1)
    servo.duty(40)
    time.sleep(1)
    servo.duty(50)
    time.sleep(1)
    servo.duty(0)
    time.sleep(1)

rotate()