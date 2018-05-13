import microbit
import radio
import math

#constants
mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 47

#setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

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
    # tot hier

    
def functie_B():
    # deze code mag je veranderen
    boat0 = microbit.Image("09990:"
                           "09090:"
                           "00000:"
                           "00000"
                           "00000")
    boat1 = microbit.Image("99999:"
                           "09990:"
                           "09090:"
                           "00000:"
                           "00000:")
    boat2 = microbit.Image("00900:"
                           "99999:"
                           "09990:"
                           "09090:"
                           "00000:")
    boat3 = microbit.Image("00000:"
                           "00900:"
                           "99999:"
                           "09990:"
                           "09090:")
    boat4 = microbit.Image("44444:"
                           "44944:"
                           "99999:"
                           "49994:"
                           "49494:")
    boat5 = microbit.Image("44444:"
                           "44944:"
                           "99999:"
                           "49994:" 
                           "49494:")
    boat6 = microbit.Image("77777:"
                           "77977:"
                           "99999:"
                           "79997:" 
                           "79797:")
    boat7 = microbit.Image("99999:"
                           "99999:"
                           "99999:"
                           "99999:" 
                           "99999:")
    boat8 = microbit.Image("00000:"
                           "00000:"
                           "00000:"
                           "00000:" 
                           "00000:")
    boat9 = microbit.Image("00000:"
                           "00100:"
                           "11111:"
                           "01110:" 
                           "01010:")
    boat10 = microbit.Image("00000:"
                           "00300:"
                           "33333:"
                           "03330:" 
                           "03030:")
    boat11 = microbit.Image("00000:"
                           "00500:"
                           "55555:"
                           "05550:" 
                           "05050:")
    boat12 = microbit.Image("00000:"
                           "00700:"
                           "77777:"
                           "07770:" 
                           "07070:")
    boat13 = microbit.Image("00000:"
                           "00900:"
                           "99999:"
                           "09990:" 
                           "09090:")
    boat14 = microbit.Image("00000:"
                           "00000:"
                           "00000:"
                           "00000:" 
                           "00000:")                       
                           

    anim = [boat0, boat1, boat2, boat3, boat4, boat5, boat6, boat7, boat8, boat9, boat10, boat11, boat12, boat13, boat14]

    microbit.display.show(anim)
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