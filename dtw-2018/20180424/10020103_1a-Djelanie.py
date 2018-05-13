from microbit import *

boat0 = Image("99999:"
              "00500:"
              "00500:"
              "00500:"
              "00500:")
boat1 = Image("00000:"
              "99999:"
              "00500:"
              "00500:"
              "00500:")
boat2 = Image("00000:"
              "00000:"
              "99999:"
              "00500:"
              "00500:")
boat3 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "00500:")
boat4 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999:")
boat5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000:")
anim = [boat5, boat4, boat3, boat2, boat1, boat0]

for i in anim:
    display.show(i)
    sleep(300)
