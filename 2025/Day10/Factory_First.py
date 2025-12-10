def main():

    fileName = "six.txt"
    path = "../../../Advent Of Code Cases/2025/Day10/" + fileName

    machines = []
    with open(path, 'r') as file:
        for line in file:
            currentLine = line.strip()
            lights = []
            buttons = []
            joltReq = []
            objects = currentLine.split(" ")
            lights = objects[0]
            joltReq = objects[len(objects)-1]
            
            buttons = objects[1:len(objects)-1]
            
            lights = list(lights)[1:len(lights)-1]            

            newButtons = []
            for button in buttons:
                button = button[1:len(button)-1].split(',')
                button = list(map(int, button))
                newButtons.append(button)
            mach = {"lights": lights, "buttons": newButtons}
            machines.append(mach)


    minCounts = 0
    print(len(machines))
    for machine in machines:
        mc = getMachineButtonCount(machine)
        print(mc)
        minCounts += mc

    print("Min count sum:",minCounts)
            

def getMachineButtonCount(machine):
    
    minCount = 0
    cache = {}
    
    def performRun(run):
        bu = run["bu"]
        li = run["li"]
        pc = run["pc"]+1
        #print(pc)
        local = []
        for l in li:
            local.append(l)
        nonlocal minCount
        applyButton(local,bu)
        #print("orig", lights)
        #print("curr", li)
        #print("is equal", li == lights)
        localAsString = ''.join(local)
        if local == lights:
            minCount = pc
        else:
            if not localAsString in cache or pc <= cache[localAsString]:
                cache[localAsString] = pc
                #print(cache)
                for button in buttons:
                    if button != bu:              
                        run = {"li": local,"bu": button, "pc": pc}
                        runQueue.append(run)
        return

                
    lights = machine["lights"]
    buttons = machine["buttons"]
    currentLights = []
    for i in range(len(lights)):
        currentLights.append('.')
    runQueue = []
    for button in buttons:
        run = {"li": currentLights,"bu": button, "pc": 0}
        runQueue.append(run)

    while len(runQueue)>0:
        currentRun = runQueue.pop(0)
        performRun(currentRun)
        #print("min",minCount)
        print(len(cache))

        if minCount > 0:
            break

    return minCount


def applyButton(currentLights,button):
    for pos in button:
        if currentLights[pos] == ".":
            currentLights[pos] = "#"
        else:
            currentLights[pos] = "."

    return currentLights

if __name__ == "__main__":
    main()
