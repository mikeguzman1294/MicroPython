import machine
import time

LED_PIN = 2 # D4
BUTTON_PIN = 13 # D5

def blink():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

    while button.value():
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    led.off()

blink()