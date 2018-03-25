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

microbit.display.show("-")

############################################
##### vanaf hier mag je code aanpassen #####
############################################



##################
### Event loop ###
##################

def get_message():
    try:
        msg = radio.receive_bytes()
        if msg is not None:
            if msg[0] == 01 and msg[1] == 00 and msg[2] == 01: #DAL-packet
#            if msg[0:2] == int("010001", 16):
                packet_type = msg[3]
#                microbit.display.scroll( str(packet_type) )
                
#                packet_time = "T:"
#                for b in msg[4:7]:
#                    packet_time += str.format("%02X" % b)
#                packet_time += " "
#                microbit.display.scroll(packet_time)
                
#                packet_id = "I:"
#                for b in msg[8:11]:
#                    packet_id += str.format("%02X" % b)
#                packet_id += " "
#                microbit.display.scroll(packet_id)
                
#                packet_payload = "P:"
#                for b in msg[12:]:
#                    packet_payload += str.format("%02X" % b)
#                packet_payload += " "
#                microbit.display.scroll(packet_payload)
                
                if packet_type == 0:
                    payload = 0
                    #microbit.display.scroll( str(len(msg[12:])) )
                    for i in range(len(msg[12:])):
                        payload += msg[12+i] * math.pow(256, i)
                        #microbit.display.scroll( str(i) +":"+str(msg[12+i] * math.pow(256, i)) )

                    #microbit.display.scroll( str( ustruct.unpack( "<i", str(msg[12:15]) ) ) )
                    microbit.display.scroll( str(int(payload)) )
                    
                
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
    # Read and parse any incoming messages
    get_message()


    # check if button A and B were pressed
    if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
        functie_AB()

    # check if button A was pressed
    elif microbit.button_a.was_pressed():
        functie_A()

    # check if button B was pressed
    elif microbit.button_b.was_pressed():
        functie_B()
