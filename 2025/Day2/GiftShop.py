def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day2/" + fileName

    
    
    with open(path, 'r') as file:
        numRanges = file.read().split(",")

    invalidSum = 0
    for numRange in numRanges:
        invalidSum += getRangeSumSimple(numRange)
        
    print("Simple:",invalidSum)

    invalidSum = 0
        
    for numRange in numRanges:
        invalidSum += getRangeSumComplex(numRange)
        
    print("Complex:",invalidSum)


def getRangeSumSimple(numRange):

    rangeSum = 0

    start = int(numRange.split("-")[0])
    end = int(numRange.split("-")[1])

    for i in range(start,end+1):
        iString = str(i)
        if len(iString) % 2 == 0: #Is even
            half = int(len(iString) / 2)
            first = iString[0:half]
            second = iString[half:half*2]
            if first == second:
                rangeSum += i
    
    return rangeSum


def getRangeSumComplex(numRange):

    rangeSum = 0

    start = int(numRange.split("-")[0])
    end = int(numRange.split("-")[1])

    for currentNumber in range(start,end+1):
        
        currentNumberString = str(currentNumber)
        length = len(currentNumberString)
        #print("Current number:",currentNumber)
        for interval in range(1,length//2+1):
            isNumberAdded = False
            if length % interval == 0: #Divisible by interval
                y = interval
                toAdd = True
                while y <= length-interval:
                    first = currentNumberString[y-interval:y]
                    second = currentNumberString[y:y+interval]
                    #print(first,second)
                    #print(y)
                    if first != second:
                        toAdd = False
                        break
                    y+=interval

                if toAdd:
                    #print("Adding", currentNumber)
                    rangeSum += currentNumber
                    isNumberAdded = True
            if isNumberAdded:
                break
    
    return rangeSum
        
if __name__ == "__main__":
    main()
