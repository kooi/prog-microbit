"""
    neopixel_random.py

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

"""
from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin0, 2)
a = 0
m = 1

while True:
    #Iterate over each LED in the strip

    red = a
    green = 0
    blue = 0

    # Assign the current LED a random red, green and blue value between 0 and 60
    np[1] = (red, green, blue)

    # Display the current pixel data on the Neopixel strip
    np.show()
    sleep(10)
    a = a + m
    if a == 255 or a == 0:
        m = -m
