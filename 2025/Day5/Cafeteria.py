def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day5/" + fileName

    ingredientRanges = []
    ingredientIDs = []

    readingRanges = True

    
    with open(path, 'r') as file:
        for line in file:
            thisLine = line.strip()

            if readingRanges:
                if not thisLine:
                    readingRanges = False
                    continue
                low = int(thisLine.split("-")[0])
                high = int(thisLine.split("-")[1])
                ingredientRanges.append([low,high])
            else:
                ingredientIDs.append(int(thisLine))
            
    validCount = 0
    for ingredientID in ingredientIDs:
        for ingredientRange in ingredientRanges:
            if ingredientID >= ingredientRange[0] and \
               ingredientID <= ingredientRange[1]:
                validCount+=1
                break

    print("Valid count:",validCount)

##    Naive approach - gets memory error
##    validIDsDict = {}
##    for ingredientRange in ingredientRanges:
##        low = ingredientRange[0]
##        high = ingredientRange[1]
##        print(low)
##        while low <= high:
##            if not low in validIDsDict:
##                validIDsDict[low] = True
##            low += 1
##
##    print("Valid ID count:",len(validIDsDict.keys()))


    currentCount = len(ingredientRanges)
    nextCount = 0
    joinedRanges = ingredientRanges
    while True:
        joinedRanges = joinRanges(joinedRanges)
        nextCount = len(joinedRanges)

        if nextCount == currentCount:
            break
        currentCount = nextCount

    #print(joinedRanges)

    expandedCount = 0
    for joinedRange in joinedRanges:
        expandedCount += joinedRange[1] - joinedRange[0] + 1
        
    print("Expanded Count:",expandedCount)

def joinRanges(rangeList):
    joinedRanges = []
    for ingredientRange in rangeList:
        if len(joinedRanges) == 0:
            joinedRanges.append(ingredientRange)
        else:
            commonFound = False
            for i in range(len(joinedRanges)):
                commonRange = joinedRanges[i]
                listOfRanges = getRangeIntersection(commonRange,ingredientRange)
                if len(listOfRanges) == 1:
                    joinedRanges[i] = listOfRanges[0]
                    commonFound = True
                    break
                if commonFound:
                    break
            if not commonFound:
                joinedRanges.append(ingredientRange)    

    return joinedRanges

def getRangeIntersection(range1,range2):
    if range2[0] < range1[0]:
        return getRangeIntersection(range2,range1)

    if range1[0] < range2[0] and range1[1] < range2[0]:
        #Range 1 whole smaller
        return [range1,range2]

    if range1[0] == range2[0] and range1[1] == range2[1]:
        #Equal ranges
        return [range1]

    if range1[0] == range2[0]:
        #Start equal
        if range1[1] < range2[1]:
            return [[range1[0],range2[1]]]
        else:
            return [[range1[0],range1[1]]]
        
    if range1[1] == range2[1]:
        #Finish equal
        if range1[0] < range2[0]:
            return [[range1[0],range1[1]]]
        else:
            return [[range2[0],range1[1]]]

    if range1[1]+1 == range2[0]:
        #Perfect overlap
        return [[range1[0],range2[1]]]

    if range1[0] < range2[0] and range1[1] > range2[1]:
        #Swallows
        return [range1]                

    # Only case left - range2 extends range1
    return [[range1[0],range2[1]]]

if __name__ == "__main__":
    main()
