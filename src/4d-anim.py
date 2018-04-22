import microbit

boat0 = microbit.Image("00500:00550:00500:99999:09990:")
boat1 = microbit.Image("00000:00500:00550:00500:99999:")
boat2 = microbit.Image("00000:00000:00500:00550:00500:")
boat3 = microbit.Image("00000:00000:00000:00500:00550:")
boat4 = microbit.Image("00000:00000:00000:00000:00500:")
boat5 = microbit.Image("00000:00000:00000:00000:00000:")

anim = [boat0, boat1, boat2, boat3, boat4, boat5, boat4, boat3, boat2, boat1]

microbit.display.show(anim, loop=True)
