import microbit
import radio
import math

#constants
mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 23

#setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################
def functie_A():
    for i in range(4):
        microbit.display.set_pixel(i, 1, 9)
    for i in range(4):
        microbit.display.set_pixel(i, 2, 9)
    for i in range(4):
        microbit.display.set_pixel(i, 3, 9)
    for i in range(4):
        microbit.display.set_pixel(i, 4, 9)
    microbit.sleep(200)
    microbit.display.clear()

    
def functie_B():
    for i in range(5):
        microbit.display.set_pixel(0, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(1, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(2, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(3, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(4, i, 9)
        microbit.sleep(25)
    microbit.sleep(200)
    microbit.display.clear()
        
            
def functie_AB():
    for i in range(5):
        microbit.display.set_pixel(1, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(2, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(3, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(4, i, 9)
        microbit.sleep(25)
    for i in range(5):
        microbit.display.set_pixel(5, i, 9)
        microbit.sleep(25)

    microbit.sleep(200)
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

    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        functie_AB()
    elif microbit.button_a.was_pressed():
        functie_A()
    elif microbit.button_b.was_pressed():
        functie_B()
