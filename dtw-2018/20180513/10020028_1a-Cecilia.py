import microbit

import radio

import math
#constants

mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 28

#setup
radio.config(group=1)
radio.on()


####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

def functie_A():
    # deze code mag je veranderen
    boat7 = microbit.Image("00000:"
                           "50000:"
                           "00000:"           
                           "55000:"
                           "00000")
    boat8 = microbit.Image("50000:"
                           "55000:"
                           "50000:"
                           "55500:"                      
                           "55000")
    boat9 = microbit.Image("05000:"
                           "05500:"
                           "05000:"
                           "55550:"
                           "55500")
    boat10 = microbit.Image("50000:"
                           "55000:"
                           "50000:"
                           "55507:"
                           "55007:")
    boat11 = microbit.Image("50000:"
                          "55000:"
                          "50000:"
                          "55507:"
                           "55007")
    boat12 = microbit.Image("00000:"
                          "50007:"
                            "00007:"
                            "55077:"
                            "50077")
    boat13 = microbit.Image("00000:"
                            "50007:"
                            "00007:"
                            "55077:"
                            "50077")
    boat14 = microbit.Image("00000:"
                            "50007:"
                            "00007:"
                            "55077:"
                            "50077")
    boat15 = microbit.Image("00007:"
                            "50077:"
                            "00077:"
                            "55777:"
                            "50777")
    boat30 = microbit.Image("00007:"
                            "50077:"
                            "00077:"
                            "55777:"
                            "50777")                        
                            
    KABOEM = microbit.Image("00000:"
                            "00000:"
                            "00900:"
                            "00000:"
                            "00000:")
    KABOEM1 = microbit.Image("00000:" 
                             "00900:"
                             "09990:"
                             "00900:"
                             "00000:")
    KABOEM2 = microbit.Image("99999:"
                             "99999:"
                             "99999:"
                             "99999:"
                             "99999:")
    boat16 = microbit.Image("00007:"
                            "50077:"
                           "00077:"
                            "55777:"
                            "50777")
    boat17 = microbit.Image("00007:"
                            "00077:"
                            "50077:"
                            "00777:"
                            "55777")

    boat18 = microbit.Image("00007:"
                            "00077:"
                            "00077:"
                            "50777:"
                            "00777")
    boat19 = microbit.Image("00007:" 
                          "00077:"
                          "00077:"
                            "00777:"
                           "50777:")
    boat20 = microbit.Image("00007:"
                            "00077:"
                            "00077:"
                            "00777:"
                            "00777:")
    pause = microbit.Image ("00000:"
                            "00000:"
                            "00000:"
                           "00000:"
                           "00000:")
    a = [boat8, boat9, boat10, boat11, boat12, boat13, boat14, boat15, boat30, KABOEM, KABOEM1, KABOEM2, boat16, boat17, boat18,  boat19, boat20, pause]
    microbit.display.show(a)
    # tot hier

def functie_B():

    # deze code mag je veranderen
    heart1 = microbit.Image("08880:"
                            "00800:"
                            "00800:"
                            "00800:"
                            "08880")
    heart2 = microbit.Image("08080:"
                            "88888:"
                            "88888:"
                            "08880:"
                            "00800")
    heart3 = microbit.Image("08080:"
                            "08080:"
                            "08080:"
                            "08080:"
                            "08880")

    anim = [heart1, heart2, heart3]
    microbit.display.show(anim)
    # tot hier
def functie_AB():
    # deze code mag je veranderen
    microbit.display.scroll("Titanic")

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