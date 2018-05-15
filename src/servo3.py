
import microbit

sv = 52 # de servo ondersteunt waarden tussen de 25 en de 125

while True:

    # Button A sends a message
    if microbit.button_a.was_pressed():
        sv = 30
        microbit.display.clear()
        microbit.display.set_pixel(0,0,9)

    # Button A sends a message
    if microbit.button_b.was_pressed():
        sv = 120
        microbit.display.clear()
        microbit.display.set_pixel(4,0,9)

    microbit.pin0.write_analog(sv)

    # hiermee haal je jitter weg, dit zou 20 moeten zijn maar zal 
    # ws afhangen van de interne weerstanden van de gebruikte servo
    microbit.pin0.set_analog_period(18)
    # evt kun je het nauwkeuriger instellen met 
    #microbit.pin0.set_analog_period_microseconds(18000)
    # je moet één van deze beide wel aanroepen na de eerste keer dat je
    # microbit.pin0.write_analog(...) aanroept

    microbit.sleep(1000) # je moet de servo even de tijd geven om te roteren
    
