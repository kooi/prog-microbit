import microbit
import radio

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
#    microbit.display.set_pixel(0,0,9)
#    sleep(5)
#    microbit.display.set_pixel(0,0,0)
    
#    microbit.display.scroll(incoming)
#    microbit.display.scroll(incoming, wait=False)
#    microbit.sleep(100)
    # parse as integer?
    print(incoming)
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

##################
### Event loop ###
##################

def get_message():
    while True:
        try:
            msg = radio.receive_bytes()
            if msg is not None:
                if len(msg)
                return str(msg[13:],'utf-8')
#                print(len(msg))
#                if len(msg) >= 13 and msg[3] == 2:
#                    lstr = msg[12] # length byte
#                    text = str(msg[13:13+lstr], 'ascii')
#                return text

        except Exception as e: # reset radio on error
            radio.off()
            radio.on()


while True:
    # Read any incoming messages
    # radio does not receive when looping?
#    incoming = radio.receive()
#    if incoming is not None:
#        microbit.display.set_pixel(0,0,9)
#        handleRadio(incoming)

#    incoming2 = radio.receive_bytes()
#    if incoming2 is not None:
#        microbit.display.set_pixel(0,4,9)
#        handleRadio(incoming)

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

