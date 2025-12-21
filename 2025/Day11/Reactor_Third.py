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


    def getCount(deviceFrom,deviceTo):
        def fillDevicePaths(deviceFrom,deviceTo):
            pathsCount = 0

            if deviceFrom == deviceTo:
                devicePathCounts[deviceFrom] = 1
                return
            if deviceFrom == "out":
                devicePathCounts[deviceFrom] = 0
                return                
                
            nextDevices = devices[deviceFrom]

            for nextDevice in nextDevices:

                if nextDevice not in devicePathCounts:
                    fillDevicePaths(nextDevice,deviceTo)

                nextDevicePathCount = devicePathCounts[nextDevice]

                pathsCount+=nextDevicePathCount

            devicePathCounts[deviceFrom] = pathsCount
            
        devicePathCounts = {}
        fillDevicePaths(deviceFrom,deviceTo) 
        return devicePathCounts[deviceFrom]
        
   
    svrOut = getCount("svr","out")
    svrDac = getCount("svr","dac")
    svrFft = getCount("svr","fft")
    dacFft = getCount("dac","fft")
    fftDac = getCount("fft","dac")
    dacOut = getCount("dac","out")
    fftOut = getCount("fft","out")
    
    print("Part 1 - SVR-OUT",svrOut)

    part2Count = svrDac * dacFft * fftOut + svrFft*fftDac*dacOut

    print("Part 2 - SVR-OUT thru dac&fft",part2Count)



if __name__ == "__main__":
    main()
