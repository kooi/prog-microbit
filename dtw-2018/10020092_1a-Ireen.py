import microbit
import radio
import math
import music

#constants
mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 92

#setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

boat0 = microbit.Image("09090:"
                       "99999:"
                       "99999:"
                       "09990:"
                       "00900")
boat1 = microbit.Image("09090:"
                       "90909:"
                       "90009:"
                       "09090:"
                       "00900")
boat2 = microbit.Image("00000:"
                       "09090:"
                       "09990:"
                       "00900:"
                       "00000:")

def functie_A():
    # deze code mag je veranderen
    microbit.display.show( boat0 )
    microbit.sleep(2000)
    microbit.display.clear()
    # tot hier


def functie_B():
    # deze code mag je veranderen
    microbit.display.show( boat1 )
    microbit.sleep(2000)
    microbit.display.clear()
    # tot hier


def functie_AB():
    # deze code mag je veranderen
    microbit.display.show( boat2 )
    microbit.sleep(2000)
    microbit.display.clear()
    # tot hier


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
        functie_A()
    elif microbit.button_b.get_presses() > 0:
        functie_B()
