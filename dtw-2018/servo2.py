import microbit

class Servo:
    def __init__(self, pin, trim=0):
        self.pin = pin
        self.trim = trim
        self.position = 90
        self.set_period()

    def set_period(self):
        self.pin.set_analog_period(20)
        self.write(self.position)
        microbit.sleep(80)
        self.pin.set_analog_period(20)
        self.write(self.position)
        microbit.sleep(80)
        self.pin.write_analog(0)

    def write(self, degrees):
        self.pin.write_analog(int(25 + 100 * degrees / 180 + self.trim))
        self.position = degrees

    def move(self, degrees, delay=4):
        if degrees > self.position:
            step = 1
        else:
            step = -1
        for position in range(self.position, degrees, step):
            self.write(position)
            microbit.sleep(delay)

#s1 = Servo(microbit.pin16, 0)

s=0

while True:
#    microbit.pin16.write_analog(int(25 + 100 * 90 / 180))
#    microbit.sleep(5000)
#    microbit.pin16.write_analog(int(25 + 100 * 0 / 180))
#    microbit.sleep(1000)
    microbit.pin1.write_analog(s)
    microbit.sleep(1000)
    s+=0.1
    microbit.display.show(str(s))
