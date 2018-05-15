import microbit

def getVarFromFile(varName, fileName="vars.txt"):
    with open(fileName, 'r') as f:
        data = f.read()
        da = data.split('=')
        for el in da:
            if el == varName:
                return int(da[da.index(el)+1])
        print (data) #--> parse and return variable
    return 0

def saveVarToFile(varName, value, fileName="vars.txt"):
    with open(fileName, 'w') as f:
        f.write(varName + '=' + str(value))

############
try:
    counter = getVarFromFile('counter')
except:
    counter = 0

while True:
    if microbit.button_a.was_pressed():
        counter = counter + 1
        saveVarToFile('counter', counter)

    if microbit.button_b.was_pressed():
        counter = counter - 1
        saveVarToFile('counter', counter)
    
    microbit.display.show(str(counter))
    microbit.sleep(1000)
        
        
