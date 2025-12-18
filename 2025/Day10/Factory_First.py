def main():

    fileName = "test.txt"
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
            lights = list(lights)[1:len(lights)-1]
            
            buttons = objects[1:len(objects)-1]
            newButtons = []
            for button in buttons:
                button = button[1:len(button)-1].split(',')
                button = list(map(int, button))
                newButtons.append(button)

            joltReq = objects[len(objects)-1]
            joltReq = list(map(int,joltReq[1:len(joltReq)-1].split(',')))
            mach = {"lights": lights, "buttons": newButtons, 'jolts': joltReq}
            machines.append(mach)
            
    #print(machines)

    lightsCount = 0
    for machine in machines:
        mc = getLightsCount(machine)
        lightsCount += mc

    print("Lights count:",lightsCount)

    joltCount = 0
    for machine in machines:
        mc = getJoltsCount(machine)
        #print(mc)
        joltCount += mc

    print("Jolt count:",joltCount)            

def getLightsCount(machine):
    
    minCount = 0
    cache = {}
    triedList = []
    
    def performRun(run):
        bu = run["bu"]
        li = run["li"]
        bp = run["bp"]

        local = []
        for l in li:
            local.append(l)
        localBP = []
        for b in bp:
            localBP.append(b)

        localBP.append(bu)

        localBP.sort()

        nonlocal minCount

        applyLightsButton(local,bu)
        localAsString = ''.join(local)

        if local == lights:

            minCount = len(localBP)
        else:
            if localAsString in cache and cache[localAsString]<len(localBP):
                return
            if localBP in triedList:
                return

            triedList.append(localBP)
            for button in buttons:
                cache[localAsString] = len(localBP)

                if not button in localBP:              
                    run = {"li": local,"bu": button, "bp": localBP}
                    runQueue.append(run)
        return

                
    lights = machine["lights"]
    buttons = machine["buttons"]
    currentLights = []
    for i in range(len(lights)):
        currentLights.append('.')
    
    runQueue = []
    for button in buttons:
        run = {"li": currentLights,"bu": button, "bp":[]}
        runQueue.append(run)

    while len(runQueue)>0:
        currentRun = runQueue.pop(0)
        performRun(currentRun)
        if minCount > 0:
            break

    return minCount

def applyLightsButton(currentLights,button):
    for pos in button:
        if currentLights[pos] == ".":
            currentLights[pos] = "#"
        else:
            currentLights[pos] = "."

    return currentLights

def getJoltsCount(machine):
    
    minCount = 0
    cache = {}
    triedList = []
    
    jolts = machine["jolts"]
    buttons = machine["buttons"]

    joltsSum = sum(jolts)
    #print(joltsSum)

    def performRun(run):
        button = run["button"]
        jolts = run["jolts"]
        buttonsPressed = run["buttonsPressed"]
        localJolts = []
        for jolt in jolts:
            localJolts.append(jolt)
        localBP = []
        for bp in buttonsPressed:
            localBP.append(bp)

        localBP.append(button)

        localBP.sort()

        nonlocal minCount

        applyJoltsButton(localJolts,button)
        localAsString = ''.join(str(localJolts))

        if min(localJolts) < 0:
            triedList.append(localBP)
            cache[localAsString] = len(localBP)
            return
        elif min(localJolts) == 0 and max(localJolts) == 0:
            minCount = len(localBP)
        else:
            if localAsString in cache and cache[localAsString]<len(localBP):
                return
            if localBP in triedList:
                #print("tried",localBP)
                return
            if len(localBP) > joltsSum:
                return

            triedList.append(localBP)
            cache[localAsString] = len(localBP)
            for newButton in buttons:
                run = {"jolts": localJolts,"button": newButton, "buttonsPressed": localBP}
                runQueue.append(run)
                
        return
    
    runQueue = []
    for button in buttons:
        run = {"jolts": jolts,"button": button, "buttonsPressed":[]}
        runQueue.append(run)

    while len(runQueue)>0:
        currentRun = runQueue.pop(0)
        performRun(currentRun)
        if minCount > 0:
            break

    return minCount

def applyJoltsButton(jolts,button):
    for pos in button:
        jolts[pos]-=1
    return jolts

if __name__ == "__main__":
    main()
