def main():

    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day11/" + fileName

    devices = {}
    with open(path, 'r') as file:
        for line in file:
            currentLine = line.strip().split(":")

            name = currentLine[0]
            outputs = currentLine[1].strip().split()
            devices[name] = outputs

    devicePaths = {}

    def fillDevicePaths(device):
  
        nextDevices = devices[device]
        #pathFromHere = [device]
        currentDevicePaths = []

        for nextDevice in nextDevices:
            if nextDevice == "out":
                nextPaths = [[nextDevice]]
            elif nextDevice in devicePaths:
                nextPaths = [[nextDevice]]
            else:
                nextPaths = fillDevicePaths(nextDevice)

            for path in nextPaths:
                localPath = [device]
                for p in path:
                    localPath.append(p)
                currentDevicePaths.append(localPath)

            
        #print(device,currentDevicePaths)
        devicePaths[device] = currentDevicePaths

        return currentDevicePaths


    fillDevicePaths("svr")
    print("Finished filling")
    
    svrPaths = devicePaths["svr"]
    print(len(svrPaths))
    #print(svrPaths)

    examinedDevicesTotals = {}
    examinedDevicesValids = {}
    def getPathData(path,hasDac,hasFft):
        #print(path,hasDac,hasFft)
        totalCount = 0
        validCount = 0

        if hasDac or "dac" in path:
            hasDac = True
            
        if hasFft or "fft" in path:
            hasFft = True

        lastElement = path[-1]     
        if lastElement == "out":
            return 1, hasDac and hasFft

        #if lastElement in examinedDevicesTotals:
        #    totalCount = examinedDevicesTotals[lastElement]
        #    validCount = examinedDevicesValids[lastElement]
        #else:
        nextPaths = devicePaths[lastElement]
        #print(nextPaths)
        for np in nextPaths:
            tc, vc = getPathData(np,hasDac,hasFft)        
            totalCount+=tc
            validCount+=vc  
            
        #if lastElement not in examinedDevicesTotals:
        #examinedDevicesTotals[lastElement] = totalCount
        #examinedDevicesValids[lastElement] = validCount 
           

        return totalCount,validCount

    totalCount = 0
    validCount = 0
    i = 1
    for path in svrPaths:        
        tc, vc = getPathData(path,False,False)
        totalCount+=tc
        validCount+=vc
        print(i,validCount)
        #print(i)
        i+=1

    print("Total path count:", totalCount)
    print("Valid path count:", validCount) 

if __name__ == "__main__":
    main()
