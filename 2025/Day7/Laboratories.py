def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day7/" + fileName

    rows = []
    with open(path, 'r') as file:
        for line in file:
            rows.append(list(line.strip()))


    startY = 0
    for i in range(len(rows[0])):
        if rows[0][i] == "S":
            rows[1][i] = "|"
            startY = i
            break


    splitCount = traversePart1(rows)
    print("Split count:", splitCount)

    pathCount = getAllPaths(rows,1,startY)
    print("Path count:",pathCount)

            
def traversePart1(rows):
    splitCount = 0
    for x in range (1, len(rows)-1):
        for y in range (len(rows[0])):
            if rows[x][y] == "|":
                if rows[x+1][y] == "^":
                    splitCount += 1
                    rows[x+1][y-1] = "|"
                    rows[x+1][y+1] = "|"
                else:
                    rows[x+1][y] = "|"

    return splitCount


def getAllPaths(rows,startX,startY):

    cache = [[0 for y in range(len(rows))] for x in range(len(rows[0]))]
    
    def getPathCount(rows,startX,startY):

        if cache[startX][startY] != 0:
            return cache[startX][startY]

        for x in range (startX+1, len(rows)-1):
            if rows[x][startY] == "^":
                pathCount = getPathCount(rows,x,startY-1) + getPathCount(rows,x,startY+1)
                cache[startX][startY] = pathCount
                return pathCount

        cache[startX][startY] = 1
        return 1

    return getPathCount(rows,startX,startY)
    
        
if __name__ == "__main__":
    main()
