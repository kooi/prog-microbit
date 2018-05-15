import microbit
import radio
import math

#constants
mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 141

#setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

def functie_A():
    # deze code mag je veranderen
    boat0 = microbit.Image("00000:"
                           "00005:"
                           "90005:"
                           "00005:"
                           "00000:")
    boat1 = microbit.Image("00000:"
                           "00005:"
                           "09005:"
                           "00005:"
                           "00000:")
    boat2 = microbit.Image("00000:"
                           "00005:"
                           "00905:"
                           "00005:"
                           "00000:")
    boat3 = microbit.Image("00000:"
                           "00005:"
                           "00095:"
                           "00005:"
                           "00000:")
    boat4 = microbit.Image("00000:"
                           "00005:"
                           "00905:"
                           "00005:"
                           "00000:")
    boat5 = microbit.Image("00000:"
                           "00005:"
                           "90005:"
                           "00005:"
                           "00000:")
    boat6 = microbit.Image("00000:"
                           "00005:"
                           "00005:"
                           "00005:"
                           "00000:")
    boat7 = microbit.Image("00555:"
                           "90505:"
                           "90555:"
                           "90500:"
                           "90500:")
    boat8 = microbit.Image("00555:"
                           "90505:"
                           "90555:"
                           "90500:"
                           "90500:")
    boat9 = microbit.Image("00555:"
                           "90505:"
                           "90555:"
                           "90500:"
                           "90500:")
    anim = [boat0, boat1, boat2, boat3, boat4, boat5, boat6, boat7, boat8, boat9]
    microbit.pin2.write_analog(30)
    for i in anim :
        microbit.display.show(i)
        microbit.sleep(300)
    # tot hier


def functie_B():
    # deze code mag je veranderen
    microbit.pin2.write_analog(90)
    microbit.display.show(
        microbit.Image( '00000:'
                        '00099:'
                        '00099:'
                        '00000:'
                        '00000:' ) )
    microbit.sleep(200)
    microbit.display.clear()
    # tot hier


def functie_AB():
    # deze code mag je veranderen
    microbit.pin2.write_analog(5)
    microbit.display.show(
        microbit.Image( '00000:'
                        '99099:'
                        '99099:'
                        '00000:'
                        '00000:' ) )
    microbit.sleep(200)
    microbit.display.clear()
    # tot hier


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

    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        functie_AB()
    elif microbit.button_a.was_pressed():
        functie_A()
    elif microbit.button_b.was_pressed():
        functie_B()