import microbit
import radio
#import math
import random
import music


# constants
mijnReserve = 0
mijnSchool = 20
mijnLeerling = 25

# setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

#bom1 = microbit.Image("00000:"
#             "09990:"
#             "99999:"
#             "90909:"
#             "00900:")



def functie_Toon_Led():
    RandomGetal = random.randint(1, 3)

    if RandomGetal == 1:
        microbit.pin1.write_analog(0)
        microbit.pin2.write_analog(255)

    if RandomGetal == 2:
        microbit.pin1.write_analog(255)
        microbit.pin2.write_analog(255)

    if RandomGetal == 3:
        microbit.pin1.write_analog(255)
        microbit.pin2.write_analog(0)

def functie_AB():
    Aftelgetal = 9
    music.set_tempo(bpm=480)

    for i in range(9):

        microbit.display.show(str(Aftelgetal))
        functie_Toon_Led()

        if Aftelgetal == 1:
            music.play('c7:4')
            music.play('c7:4')
        else:
            music.play('c7:8')

        microbit.pin1.write_analog(0)
        microbit.pin2.write_analog(0)

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

        microbit.pin1.write_analog(0)
        microbit.pin2.write_analog(0)

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

#    microbit.display.show(bom1)

    microbit.sleep(1000)
    microbit.display.clear()


############################################
###### tot hier mag je code aanpassen ######
############################################

def handleRadio(incoming):
    receivedNumber = float(incoming)
    nummerOntvangen = receivedNumber
    nummerKnopje    = int(nummerOntvangen / 1000000)
    nummerOntvangen = nummerOntvangen - nummerKnopje * 1000000
    nummerReserve   = int(nummerOntvangen / 100000)
    nummerOntvangen = nummerOntvangen - nummerReserve* 100000
    nummerSchool    = int(nummerOntvangen / 1000)
    nummerOntvangen = nummerOntvangen - nummerSchool * 1000
    nummerLeerling  = int(nummerOntvangen)

    if nummerReserve  == mijnReserve  or nummerReserve  == 0 :
        if nummerSchool   == mijnSchool   or nummerSchool   == 0:
            if nummerLeerling == mijnLeerling or nummerLeerling == 0:
                if nummerKnopje == 1:
                    #microbit.pin5.write_digital(0)
                    #microbit.sleep(50)
                    #microbit.pin5.write_digital(1)
                    functie_AB()
                elif nummerKnopje == 2:
                    #microbit.pin11.write_digital(0)
                    #microbit.sleep(50)
                    #microbit.pin11.write_digital(1)
                    functie_AB()
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
            if int(msg[0]) == 01 and int(msg[1]) == 00 and int(msg[2]) == 01:
                packet_type = msg[3]
                if packet_type == 0:
                    payload = 0
                    for i in range(len(msg[12:])):
                        payload += msg[12+i] * math.pow(256, i)
                    handleRadio(payload)
    except Exception as e:
        radio.off()
        radio.on()


while True:
    get_message()

    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        functie_AB()
    elif microbit.button_a.get_presses() > 0:
        functie_AB()
    elif microbit.button_b.get_presses() > 0:
        functie_AB()