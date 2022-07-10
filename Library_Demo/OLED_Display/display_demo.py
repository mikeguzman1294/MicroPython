from machine import Pin, I2C
import ssd1306 as ssd1306
import framebuf
from pbm_buffer import load_pbm_image

def demo():
    i2c = I2C(scl=Pin(22), sda=Pin(21))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)

    happy = load_pbm_image('heart_rot.pbm')

    display.fill(0)
    display.blit(happy, 37, 5)
    display.show()