# Author: Miguel Angel Guzman Sanchez

# Custom library to include a function able to convert a pbm image
# into a readable buffer for a OLED screen

import framebuf

def load_pbm_image(filename):
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        width, height = [int(v) for v in f.readline().split()]
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)