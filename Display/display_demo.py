from machine import Pin, I2C
import ssd1306
import framebuf
from printer import load_image


i2c = I2C(scl=Pin(22), sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)


happy = load_image('heart.pbm')

display.fill(0)
display.blit(happy, 37, 5)
display.show()