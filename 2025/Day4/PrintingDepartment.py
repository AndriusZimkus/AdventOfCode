def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day4/" + fileName

    rows = []
    
    with open(path, 'r') as file:
        for line in file:
            row = list(line.strip())
            rows.append(row)
        
    canBeAccessedCount,rows = getMatrixCount(rows)

    print("First run:",canBeAccessedCount)
    totalCount = canBeAccessedCount
    nextCount = 0

    while True:
        nextCount,rows = getMatrixCount(rows)
        if nextCount == 0:
            break

        totalCount += nextCount

    print("All runs:",totalCount)

def getMatrixCount(rows):

    wasPaper = {}
    def canBeAccessed(rows,x,y):
        if not isPaper(rows,x,y):
            return False
        else:
            adjPaperCount = getSum(rows,x,y)
                                  
            return adjPaperCount < 4

    def getSum(rows,x,y):
        totalSum = 0
        totalSum += int(isPaper(rows,x-1,y-1))
        totalSum += int(isPaper(rows,x,y-1))
        totalSum += int(isPaper(rows,x+1,y-1))
        totalSum += int(isPaper(rows,x-1,y))
        totalSum += int(isPaper(rows,x+1,y))
        totalSum += int(isPaper(rows,x-1,y+1))
        totalSum += int(isPaper(rows,x,y+1))
        totalSum += int(isPaper(rows,x+1,y+1))
                        
        return totalSum

    def isPaper(rows,x,y):
        if x<0 or y < 0 or x >= len(rows) or y>=len(rows[0]):
            return False
        else:
            key = str(x)+"-"+str(y)
            return rows[x][y] == "@" or (key in wasPaper.keys() and wasPaper[str(x)+"-"+str(y)])
                                                 
    canBeAccessedCount = 0
    for x in range(len(rows)):
        for y in range(len(rows[x])):
            thisCanBeAccessed = canBeAccessed(rows,x,y)
            if thisCanBeAccessed:
                key = str(x)+"-"+str(y)
                wasPaper[key] = True
                rows[x][y] = "."
            
            canBeAccessedCount += int (thisCanBeAccessed)
            
    return canBeAccessedCount, rows


if __name__ == "__main__":
    main()
