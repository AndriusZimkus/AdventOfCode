def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day6/" + fileName

    with open(path, 'r') as file:
        sets = {}
        for line in file:
            i = 0
            row = line.strip().split()
            for i in range(len(row)):
                if i in sets.keys():
                    sets[i].append(row[i])
                else:
                    sets[i] = [row[i]]

    total = getSetsTotal(sets)
    print ("First total: ", total)

    listsForSets = []
    with open(path, 'r') as file:
        sets = {}
        for line in file:
            listsForSets.append(list(line))

    sets = {}


    setKey = 0
    length = len(listsForSets[0])-1

    column = length - 1
    symbolFound = False

    while column >= 0:
        currentNumber = 0
        for row in range(len(listsForSets)):
            
            currentList = listsForSets[row]
            
            currentSymbol = currentList[column].strip()

            if currentSymbol == "*" or currentSymbol == "+":
                symbolFound = True
  
            else:
                if currentSymbol:
                    currentNumber = currentNumber*10 + int(currentSymbol)
                
        if currentNumber > 0:
            if setKey in sets:
                sets[setKey].append(currentNumber)
            else:   
                sets[setKey] = [currentNumber]
        column-=1

        if symbolFound:
            symbolFound = False
            sets[setKey].append(currentSymbol)
            setKey += 1

    total = getSetsTotal(sets)
    print ("Second total: ", total)


def getSetsTotal(sets):
    total = 0
    for key in sets.keys():
        currentSet = sets[key]
        action = currentSet[len(currentSet)-1]
        if action == '*':
            current = 1
        else:
            current = 0
        for i in range(len(currentSet)-1):
            if action == '*':
                current*=int(currentSet[i])
            else:
                current+=int(currentSet[i])

        total += current

    return total

if __name__ == "__main__":
    main()
