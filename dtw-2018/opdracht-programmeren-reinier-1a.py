from microbit import *

import microbit
import radio
import math
import random
import music


# constants
mijnReserve = 0
mijnSchool = 22
mijnLeerling = 120

# setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

bom0 = Image("00000:"
             "00000:"
             "09990:"
             "09990:"
             "00900:")

bom1 = Image("00000:"
             "09990:"
             "99999:"
             "90909:"
             "00900:")

bom2 = Image("09990:"
             "99999:"
             "90909:"
             "90909:"
             "00900:")

anim = [bom0, bom1, bom2]


def functie_Toon_Led():
    RandomGetal = random.randint(1, 3)

    if RandomGetal == 1:
        pin1.write_analog(0)
        pin2.write_analog(255)

    if RandomGetal == 2:
        pin1.write_analog(255)
        pin2.write_analog(255)

    if RandomGetal == 3:
        pin1.write_analog(255)
        pin2.write_analog(0)


def functie_A():
    for i in range(20):

        functie_Toon_Led()

        sleep(250)

        pin1.write_analog(0)
        pin2.write_analog(0)

        sleep(250)

    microbit.sleep(1000)
    microbit.display.clear()


def functie_B():
    Aftelgetal = 9
    for i in range(9):

        display.show(str(Aftelgetal))

        functie_Toon_Led()

        sleep(250)

        pin1.write_analog(0)
        pin2.write_analog(0)

        sleep(250)

        functie_Toon_Led()

        sleep(250)

        pin1.write_analog(0)
        pin2.write_analog(0)

        sleep(250)

        Aftelgetal = Aftelgetal - 1

    for i in anim:
        display.show(i)
        sleep(300)

    microbit.sleep(1000)
    microbit.display.clear()


def functie_AB():
    Aftelgetal = 9
    music.set_tempo(bpm=480)

    for i in range(9):

        display.show(str(Aftelgetal))
        functie_Toon_Led()

        if Aftelgetal == 1:
            music.play('c7:4')
            music.play('c7:4')
        else:
            music.play('c7:8')

        pin1.write_analog(0)
        pin2.write_analog(0)

        if Aftelgetal > 3:
            music.play('r7:8')
        elif Aftelgetal == 1:
            music.play('c7:4')
            music.play('c7:4')
        else:
            music.play('c7:8')

        functie_Toon_Led()

        if Aftelgetal > 6:
            music.play('r7:8')
        elif Aftelgetal == 1:
            music.play('c7:4')
            music.play('c7:4')
        else:
            music.play('c7:8')

        pin1.write_analog(0)
        pin2.write_analog(0)

        if Aftelgetal > 3:
            music.play('r7:8')
        elif Aftelgetal == 1:
            music.play('c7:4')
            music.play('c7:4')
        else:
            music.play('c7:8')

        Aftelgetal = Aftelgetal - 1

        if Aftelgetal == 0:
            music.play('c7:32')

    for i in anim:
        display.show(i)
        sleep(300)

    microbit.sleep(1000)
    microbit.display.clear()


############################################
###### tot hier mag je code aanpassen ######
############################################

def handleRadio(incoming):
    receivedNumber = int(incoming)
    nummerOntvangen = receivedNumber
    nummerKnopje    = nummerOntvangen / 1000000
    nummerOntvangen = nummerOntvangen - nummerKnopje * 1000000
    nummerReserve   = nummerOntvangen / 100000
    nummerOntvangen = nummerOntvangen - nummerReserve* 100000
    nummerSchool    = nummerOntvangen / 1000
    nummerOntvangen = nummerOntvangen - nummerSchool * 1000
    nummerLeerling  = nummerOntvangen

    if nummerReserve  == mijnReserve  or nummerReserve  == 0 :
        if nummerSchool   == mijnSchool   or nummerSchool   == 0:
            if nummerLeerling == mijnLeerling or nummerLeerling == 0:
                if nummerKnopje == 1:
                    #microbit.pin5.write_digital(0)
                    #microbit.sleep(50)
                    #microbit.pin5.write_digital(1)
                    functie_A()
                elif nummerKnopje == 2:
                    #microbit.pin11.write_digital(0)
                    #microbit.sleep(50)
                    #microbit.pin11.write_digital(1)
                    functie_B()
                else:
                    #microbit.pin5.write_digital(0)
                    #microbit.pin11.write_digital(0)
                    #microbit.sleep(50)
                    #microbit.pin5.write_digital(1)
                    #microbit.pin11.write_digital(1)
                    functie_AB()


def get_message():
    try:
        msg = radio.receive_bytes()
        if msg is not None:
            if msg[0] == 01 and msg[1] == 00 and msg[2] == 01:
                packet_type = msg[3]
                if packet_type == 0:
                    payload = 0
                    for i in range(len(msg[12:])):
                        payload += msg[12+i] * math.pow(256, i)
    except Exception as e:
        radio.off()
        radio.on()


while True:
    get_message()

#    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
#        functie_AB()
#    elif microbit.button_a.was_pressed():
#        functie_A()
#    elif microbit.button_b.was_pressed():
#        functie_B()

    if button_a.is_pressed() and button_b.is_pressed():
        functie_AB()
    elif button_a.is_pressed():
        functie_A()
    elif button_b.is_pressed():
        functie_B()
    sleep(100)
