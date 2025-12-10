def main():

    fileName = "input.txt"
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

    for machine in machines:
        mc = getMachineButtonCount(machine)
        minCounts += mc

    print("Min count sum:",minCounts)
            

def getMachineButtonCount(machine):
    
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

        applyButton(local,bu)
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


def applyButton(currentLights,button):
    for pos in button:
        if currentLights[pos] == ".":
            currentLights[pos] = "#"
        else:
            currentLights[pos] = "."

    return currentLights

if __name__ == "__main__":
    main()
