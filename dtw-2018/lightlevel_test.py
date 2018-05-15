# Write your code here :-)

from microbit import *


while True:
    setDisplayMode(DISPLAY_MODE_GREYSCALE);
    a = display.readLightLevel()
    sleep(100)
    display.show(a)