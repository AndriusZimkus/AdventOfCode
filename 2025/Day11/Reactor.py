def main():

    fileName = "test2.txt"
    path = "../../../Advent Of Code Cases/2025/Day11/" + fileName

    devices = {}
    with open(path, 'r') as file:
        for line in file:
            currentLine = line.strip().split(":")

            name = currentLine[0]
            outputs = currentLine[1].strip().split()
            devices[name] = outputs

    queue = []
    count = 0
    if "you" in devices:
        for out in devices["you"]:
            queue.append(out)


    while len(queue) > 0:
        current = queue.pop(0)

        if current == "out":
            count += 1
        else:
            for out in devices[current]:
                queue.append(out)

    print("Total paths, part 1:",count)

    queue = []
    count = 0
    if "svr" in devices:
        for out in devices["svr"]:
            obj = {"next":out,"path":["svr"]}
            queue.append(obj)


    count = 0
    reaches = []
    thruTarget = []
    hasDac = []
    hasFft = []
    fCount = 0
    allPaths = []
    
    def traverse(devices,nextOut,path):
        queue = []
        nonlocal count
        nonlocal fCount
        nonlocal reaches
        
        if nextOut == "out" or nextOut in reaches:

            count+=1
            allPaths.append(path)
            for p in path:
                if p not in reaches:
                    reaches.append(p)

            if "dac" in path:
                for p in path:
                    if p not in hasDac:
                        hasDac.append(p)
                        
            if "fft" in path:
                for p in path:
                    if p not in hasFft:
                        hasFft.append(p)

            for p in path:
                if p in hasDac and p in hasFft:
                    fCount += 1
                    break
                    #print("here")
                
            return
        
        for out in devices[nextOut]:
            obj = {"next":out,"path":path}
            queue.append(obj)
                      
        for obj in queue:
            nextOut = obj["next"]
            path = obj["path"]
            nextPath = []
            for p in path:
                nextPath.append(p)

            nextPath.append(nextOut)

            if nextOut == ["out"] or nextOut in path:
                continue
            
            traverse(devices,nextOut,nextPath)

    traverse(devices,"svr",[])

    #print(count)
    #for obj in queue:
    #    nextOut = obj["next"]
    #    path = traverse(devices,nextOut)

    #reaches = []

##    while len(queue) > 0:
##
##        current = queue.pop(0)
##
##        nextOut = current["next"]
##        path = current["path"]
##        newPath = []
##        for p in path:
##            newPath.append(p)
##
##        if nextOut == "out":
##            count+=1
##        else:
##            newPath.append(nextOut)
##            for out in devices[nextOut]:
##                obj = {"next":out,"path":newPath}
##                queue.append(obj)
    print("Total paths, part 2:",count)               
    print("Valid paths, part 2:",fCount)
    for p in allPaths:
        if "dac" in p or "fft" in p:
            print(p)



        

if __name__ == "__main__":
    main()
