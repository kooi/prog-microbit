import microbit
import radio
import math

#constants
mijnReserve  = 0
mijnSchool   = 20
mijnLeerling = 111

#setup
radio.config(group=1)
radio.on()

####################################################
##### vanaf hier mag je stukjes code aanpassen #####
####################################################

def functie_A():
    # deze code mag je veranderen
    tv0 = microbit.Image('50000:'
                         '55000:'
                         '50000:'
                         '99900:'
                         '99000:' ) 
    tv1 = microbit.Image('05000:'
                         '05500:'
                         '05000:'
                         '99990:'
                         '99900:' ) 
    tv2 = microbit.Image('00500:'
                         '00550:'
                         '00500:'
                         '99999:'
                         '09990:' ) 
    tv3 = microbit.Image('00050:'
                         '00055:'
                         '00050:'
                         '09999:'
                         '00999:' ) 
    tv4 = microbit.Image('00005:'
                         '00005:'
                         '00005:'
                         '00999:'
                         '00099:' ) 
    tv5 = microbit.Image('00000:'
                         '00000:'
                         '00000:'
                         '00099:'
                         '00009:' )

    anim = [tv0,tv1,tv2,tv3,tv4,tv5]

    for i in anim:
        microbit.display.show(i)
        microbit.sleep(200)   
    # tot hier

    
def functie_B():
    # deze code mag je veranderen
    tv0 = microbit.Image('00700:'
                         '07770:'
                         '07770:'
                         '77777:'
                         '00800:' ) 
    tv1 = microbit.Image('00700:'
                         '06770:'
                         '07760:'
                         '76777:'
                         '00800:' ) 
    tv2 = microbit.Image('00700:'
                         '09770:'
                         '07790:'
                         '79777:'
                         '00800:' ) 
    tv3 = microbit.Image('00700:'
                         '09770:'
                         '07790:'
                         '79777:'
                         '00800:' ) 
    tv4 = microbit.Image('00700:'
                         '08770:'
                         '07780:'
                         '78777:'
                         '00800:' ) 
    tv5 = microbit.Image('00700:'
                         '06770:'
                         '07760:'
                         '76777:'
                         '00800:' ) 
                             
    anim = [tv0,tv1,tv2,tv3,tv4,tv5]

    for i in anim:
        microbit.display.show(i)
        microbit.sleep(200)  
    # tot hier

    
def functie_AB():
    # deze code mag je veranderen
    tv0 = microbit.Image('00000:'
                         '05050:'
                         '00000:'
                         '07770:'
                         '70007:' ) 
    tv1 = microbit.Image('00000:'
                         '07070:'
                         '00000:'
                         '07770:'
                         '70007:' ) 
    tv2 = microbit.Image('00000:'
                         '09090:'
                         '00000:'
                         '07770:'
                         '70007:' ) 
    tv3 = microbit.Image('00000:'
                         '09090:'
                         '00000:'
                         '70007:'
                         '07770:' ) 
    tv4 = microbit.Image('00000:'
                         '07070:'
                         '00000:'
                         '70007:'
                         '07770:' ) 
    tv5 = microbit.Image('00000:'
                         '05050:'
                         '00000:'
                         '70007:'
                         '07770:' )

    anim = [tv0,tv1,tv2,tv3,tv4,tv5]

    for i in anim:
        microbit.display.show(i)
        microbit.sleep(200)   
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