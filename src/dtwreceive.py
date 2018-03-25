import microbit
import radio
import math

#constants
mijnReserve  = 0
mijnSchool   = 22
mijnLeerling = 120

#setup
radio.config(group=1)
radio.on()

############################################
##### vanaf hier mag je code aanpassen #####
############################################

def functie_A():
    # deze code mag je veranderen
    microbit.display.show( 
        microbit.Image( '00000:'
                        '99000:'
                        '99000:'
                        '00000:'
                        '00000:' ) )
    microbit.sleep(200)
    microbit.display.clear()
#    handleRadio("1")
    # tot hier

    
def functie_B():
    # deze code mag je veranderen
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
    nummerSchool    = nummerOntvangen / 100
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

##################
### Event loop ###
##################

def get_message():
    while True:
        try:
            msg = radio.receive_bytes()
            if msg is not None:

                if msg[0] == 01 and msg[1] == 00 and msg[2] == 01: #DAL-packet
                    if msg[3] == 0:
                        payload = 0
                        for i in range(len(msg[12:])):
                            payload += msg[12+i] * math.pow(256, i)
                        handleRadio(payload)
#                        microbit.display.scroll( str(int(payload)) )
                else:
                    line = "MSG:"
                    for b in msg:
                        line += str.format("%02X " % b)
                    microbit.display.scroll(line)

        except Exception as e:
            # reset the radio if it crashes
            microbit.display.scroll("  RESET:%s" % str(e))
            radio.off()
            radio.on()

while True:
    get_message()

    # check if button A and B were pressed
    # handles later?, use get_presses?
    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
    #if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        functie_AB()

    # check if button A was pressed
    # (handles later?)
    elif microbit.button_a.was_pressed():
        functie_A()

    # check if button B was pressed
    # (handles later?)
    elif microbit.button_b.was_pressed():
        functie_B()
