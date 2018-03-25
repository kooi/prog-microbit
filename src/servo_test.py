from microbit import *

from servo import Servo

while True:
    Servo(pin0).write_angle(0)
    sleep(200)
    Servo(pin0).write_angle(90)
    sleep(200)
    Servo(pin0).write_angle(180)
    sleep(200)