########## DIGITAL MANUFACTURING ##########
# PIKACHU Project
# Authors: Miguel Angel Guzman
#          Kadriye Nur Bakirci
###########################################

########## IMPORT REQUIRED LIBRARIES ##########

import bluetooth
from ble_uart_peripheral import BLEUART
from machine import Pin, I2C, PWM
import ssd1306 as ssd1306
from pbm_buffer import load_pbm_image
import time
import utime

########## GLOBAL VARIABLES AND PIN CONFIG ##########

# Configure LED pins for cheeks
left_cheek = Pin(19, Pin.OUT)
right_cheek = Pin(33, Pin.OUT)

# Configure Pins 22 and 21 as I2C Pins
i2c = I2C(scl=Pin(22), sda=Pin(21))
# Create a OLED display object and connect it to active I2C bus
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize Pin 26 as PWM output with =% duty cycle and 50 Hz
servo = PWM(Pin(26), freq=50, duty=0)

# Create BLE object
ble = bluetooth.BLE()
# Open UART session for BLE
uart = BLEUART(ble)

# Load all pbm images into 2-tuple buffer variables
happy_icon = (load_pbm_image("heart_rot.pbm"), load_pbm_image("heart_rot_fill.pbm"))
angry_icon = (load_pbm_image("angry_rot.pbm"), load_pbm_image("angry_rot_fill.pbm"))
sad_icon = (load_pbm_image("cry_rot.pbm"), load_pbm_image("cry_rot_2.pbm"))

# Initialize icons to happy icons
#current_image = happy_icon

########## DEFINITION OF AUX FUNCTIONS ##########

# Function that prints a buffered icon into OLED screen
def print_image(icon, display):
    display.fill(0)
    display.blit(icon, 37, 5)
    display.show()

# Function that turns on both cheek LEDS
def cheeks_on():
    left_cheek.on()
    right_cheek.on()

# Function that turns off both cheek LEDS
def cheeks_off():
    left_cheek.off()
    right_cheek.off()

# Auxiliary function that drives PWM for servo for a given angle
def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.duty(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

def wave_tail():
    for angle in range(91):
        setServoAngle(servo, angle)
        utime.sleep_ms(1)
        continue
    for angle in range(91, -1, -1):
        setServoAngle(servo, angle)
        utime.sleep_ms(1)

########## INTERRUPT SERVICE ROUTINE ##########

# Define ISR for an UART input on BLE connection
def on_rx():

    # Read UART string, AppInventor sends raw bytes
    uart_in = uart.read()
    # For some reason the UTF8 decoded string cannot be used for comparison
    # uart_in = uart.read().decode().strip()

    # Define global icon tuple variable in the scope of irq
    global current_image
    
    if uart_in == b'\x01':
        current_image = happy_icon
        
    elif uart_in == b'\x02':
        current_image = angry_icon

    elif uart_in == b'\x03':
        current_image = sad_icon

    elif uart_in == b'\x04':
        cheeks_off()

    elif uart_in == b'\x05':
        cheeks_on()

    elif uart_in == b'\x06':
        wave_tail()
    
    print("UART IN: ", uart_in)
  
# Map ISR to UART read interrupt
uart.irq(handler=on_rx)

# Set isr global variable to a default icon
current_image = happy_icon

########## DEFINITION OF MAIN DEMO ##########

def demo():
       
    # Toggle the OLED animations until interrupt is serviced
    try:
        while True:
            print_image(current_image[0], display)
            time.sleep_ms(1000)
            print_image(current_image[1], display)
            time.sleep_ms(1000)
    except KeyboardInterrupt:
        pass

    uart.close()