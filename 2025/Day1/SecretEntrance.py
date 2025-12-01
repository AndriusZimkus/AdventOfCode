def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day1/" + fileName

    rotations = []
    
    with open(path, 'r') as file:
        for line in file:
            rotations.append(line.strip())

    currentPos = 50
    countOfClicksSimple = 0
    countOfClicksComplex = 0

    for rotation in rotations:
        currentPos, clickCount = applyRotation(currentPos, rotation, "simple")
        countOfClicksSimple += clickCount

    currentPos = 50

    for rotation in rotations:
        currentPos, clickCount = applyRotation(currentPos, rotation, "0x434C49434B")
        countOfClicksComplex += clickCount


    print("Simple: ", countOfClicksSimple)
    print("0x434C49434B: ", countOfClicksComplex)
        
def applyRotation(currentPos, rotation, method):

    clickCount = 0
    direction = rotation[0]
    
    amount = int(rotation[1:])
    complexClicks = amount // 100
    amount = amount%100

    
    if direction == "L":
        finalPos = currentPos - amount
        if finalPos < 0:
            if method == "0x434C49434B" and currentPos != 0:
                clickCount += 1
            finalPos = 100 + finalPos
        elif finalPos == 0 and method == "0x434C49434B":
            clickCount += 1
    else:
        finalPos = currentPos + amount
        if finalPos >= 100:
            if method == "0x434C49434B" and currentPos != 0:
                clickCount += 1
            finalPos %= 100


    if method == "0x434C49434B":
        clickCount += complexClicks
    elif method == "simple" and finalPos == 0:
        clickCount += 1

    return finalPos,clickCount
        
if __name__ == "__main__":
    main()
