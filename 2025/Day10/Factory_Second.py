machineVariants = {}
stateCount = {}
def main():
#https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
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
           

    lightsCount = 0
    for machine in machines:

        lights = machine["lights"]
        buttons = machine["buttons"]
        variants = getVariants(lights,buttons)
        mc = 0
        for i in variants:
            if mc == 0 or len(i) < mc:
                mc = len(i)
        lightsCount += mc

    print("Lights count:", lightsCount)

    joltCount = 0
    #print(len(machines))
    for machine in machines:
        machineVariants = {}
        global stateCount
        stateCount = {}
        buttons = machine["buttons"]
        jolts = machine["jolts"]
        mc = getJoltsCount(buttons,jolts)

        print(mc)
        if mc>100000:
            print(mc,machine)
            mc = 0

        joltCount += mc
        

    print("Jolt count:",joltCount)
    


def getVariants(lights,buttons):
    
    variants = []
    
    def performRun(run):
        buttonIndex = run["buttonIndex"]
        li = run["li"]
        bp = run["bp"]

        local = []
        for l in li:
            local.append(l)
        localBP = []
        for b in bp:
            localBP.append(b)

        localBP.append(buttons[buttonIndex])

        nonlocal variants

        applyLightsButton(local,buttons[buttonIndex])

        if local == lights:
            variants.append(localBP)
        #else:
        for i in range(buttonIndex+1,len(buttons)):
            run = {"li": local,"buttonIndex": i, "bp": localBP}
            runQueue.append(run)  

        return
                
    currentLights = []
    for i in range(len(lights)):
        currentLights.append('.')
    
    runQueue = []
    for i in range(len(buttons)):
        run = {"li": currentLights,"buttonIndex": i, "bp":[]}
        runQueue.append(run)

    while len(runQueue)>0:
        currentRun = runQueue.pop(0)
        performRun(currentRun)

    return variants

def applyLightsButton(currentLights,button):
    for pos in button:
        if currentLights[pos] == ".":
            currentLights[pos] = "#"
        else:
            currentLights[pos] = "."

    return currentLights

def getJoltsCount(buttons,jolts):
    #print("entering",jolts)
    #print(stateCount)

    if max(jolts) == 0 and min(jolts) == 0:
        #print("saving",jolts,0)
        localHash = hash(tuple(jolts))
        stateCount[localHash] = 0
        #print("ret")
        return 0
    
    if min(jolts) < 0:
        #print("ret")
        return 1000000

    lights = []
    isAllEven = True
    for i in range(len(jolts)):
        if jolts[i]%2 == 1:
            lights.append("#")

            isAllEven = False
        else:
            lights.append(".")

    firstTotal = -1
    if isAllEven:
        localJolts = []
        for j in jolts:
            localJolts.append(j)
        localJolts = list(map(lambda x: x // 2 ,localJolts))

        #localHash = hash(tuple(localJolts))

##        if localHash in stateCount:
##            total = stateCount[localHash]
##        else:
##            total = 2*getJoltsCount(buttons,localJolts)
##            stateCount[localHash] = total

        firstTotal = 2*getJoltsCount(buttons,localJolts)
        #print("FT",localJolts,firstTotal)
        #return firstTotal

    localAsString = ''.join(lights)

    #print("Getting variants",lights)
    #if localAsString in machineVariants:
        #variants = machineVariants[localAsString]
    #else:
    variants = getVariants(lights,buttons)
        #machineVariants[localAsString] = variants
    #print("Variants done",len(variants),variants)
    
    if len(variants) == 0:
        if firstTotal > 0:
            return firstTotal
        #print("no variants")
        return 1000000
    
    minCount = 0
    
    for v in variants:

        localJolts = []
        for j in jolts:
            localJolts.append(j)

        for b in v:
            for p in b:
                localJolts[p]-=1

        localJolts = list(map(lambda x: x // 2 ,localJolts))
        localHash = hash(tuple(localJolts))
        #print(frozenset(localJolts))
        if localHash in stateCount:
            #print("found",localJolts)
            total = len(v) + 2*stateCount[localHash]
            #print("found result",localJolts,total,stateCount[localHash])
        else:
            #print("calculating",localJolts)
            other = 2*getJoltsCount(buttons,localJolts)
            leng = len(v)
            total = leng + other
            #print("calculated",localJolts,total)


            
        #print(localBP)
        #other = 2*getJoltsCount(buttons,localJolts)
        #leng = len(v)
        #total = leng + other

        if minCount == 0 or total < minCount:
            minCount = total

    #print("saving",jolts,minCount)
    localHash = hash(tuple(jolts))
    if firstTotal > 0 and firstTotal < minCount:
        minCount = firstTotal
    stateCount[localHash] = minCount
    
    return minCount


if __name__ == "__main__":
    main()
