def main():

    def arePointsValid(x1,y1,x2,y2,hLines,vLines):

        point1 = [x1,y1]
        point2 = [x1,y2]
        point3 = [x2,y1]
        point4 = [x2,y2]
        
        return isPointValid(point1,hLines,vLines)\
               and isPointValid(point2,hLines,vLines)\
               and isPointValid(point3,hLines,vLines)\
               and isPointValid(point4,hLines,vLines)


    def isPointValid(point,hLines,vLines):

        x = point[0]
        y = point[1]

        currHash = str(x)+"-"+str(y)
        if currHash in cache:
            return cache[currHash]
        #print("Checking:",x,y)
        
        isTopOk = False
        isBottomOk = False
        isRightOk = False
        isLeftOk = False
        
        for hLine in hLines:
            if x>=hLine.x1 and x<=hLine.x2:
                if hLine.y <= y:
                    isTopOk = True
                    topHLine = hLine

                if hLine.y >= y:
                    isBottomOk = True
                    bottomHLine = hLine                    
            if isTopOk and isBottomOk:
                break
            
        for vLine in vLines:
            if y>=vLine.y1 and y<=vLine.y2:
                if vLine.x <= x:
                    isLeftOk = True
                    leftVLine = vLine
                if vLine.x >= x:
                    isRightOk = True
                    rightVLine = vLine
            if isLeftOk and isRightOk:
                break

        isValid = isTopOk and isBottomOk and isLeftOk and isRightOk
        cache[currHash] = isValid
        if x== 17561  and y == 14395:
            print("Here:",isValid)
            print("top",topHLine)
            print("bottom",bottomHLine)
            print("left",leftVLine)
            print("right",rightVLine)
        return isValid

    
    fileName = "test.txt"
    path = "../../../Advent Of Code Cases/2025/Day9/" + fileName

    points = []
    maxX = 0
    maxY = 0
    with open(path, 'r') as file:
        for line in file:
            curr = line.strip()
            point = list(map(int,curr.split(",")))
            if point[0] > maxX:
                maxX = point[0]
            if point[1] > maxY:
                maxY = point[1]
            points.append(point)

    
    maxArea = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1 = points[i][0]
            x2 = points[j][0]
            y1 = points[i][1]
            y2 = points[j][1]
            currentArea = (abs(x1-x2)+1)*\
                          (abs(y1-y2)+1)
            if currentArea > maxArea:
                maxArea = currentArea
            

    print("Part 1 max area:", maxArea)

    horizontalLines = []
    points.sort(key=lambda x: x[1])
    for i in range(len(points)):
        if i == 0:
            previousY = points[i][1]
            previousX = points[i][0]
            currentX = 0
            currentY = 0         
        else:
            currentY = points[i][1]
            currentX = points[i][0]

            if previousY == currentY:
                #print("Curr",currentX,previousX)
                fr = min(currentX,previousX)
                to = max(currentX,previousX)
                horizontalLines.append(LineHorizontal(currentY,fr,to))

            previousY = currentY
            previousX = currentX
            

    verticalLines = []
    points.sort(key=lambda x: x[0])
    for i in range(len(points)):
        if i == 0:
            previousY = points[i][1]
            previousX = points[i][0]
            currentX = 0
            currentY = 0         
        else:
            currentY = points[i][1]
            currentX = points[i][0]

            if previousX == currentX:
                #print("Curr",currentX,previousX)
                fr = min(currentY,previousY)
                to = max(currentY,previousY)
                verticalLines.append(LineVertical(currentX,fr,to))

            previousY = currentY
            previousX = currentX


##    for line in horizontalLines:
##        print("HLine",line.y,line.x1,line.x2)
##    for line in verticalLines:
##        print("VLine",line.x,line.y1,line.y2)

    #print(len(horizontalLines))
    #print(len(verticalLines))

    maxArea = 0
    cache = {}
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            
            # Are all 4 points in area?
            isValid = arePointsValid(x1,y1,x2,y2,horizontalLines,verticalLines)
            if isValid:
                currentArea = (abs(x1-x2)+1)*\
                              (abs(y1-y2)+1)
                if currentArea > maxArea:
                    topX1 = x1
                    topX2 = x2
                    topY1 = y1
                    topY2 = y2
                    maxArea = currentArea
            

    print("Part 2 max area:", maxArea)
    print("Top x1 y1 x2 y2:", topX1,topY1, topX2, topY2)

class LineHorizontal():
    def __init__(self,y,x1,x2):
        self.y = y
        if x2>x1:
            self.x1 = x1
            self.x2 = x2
        else:
            self.x2 = x1
            self.x1 = x2
    def __str__(self):
        return "y = " + str(self.y) + " x1 = " + str(self.x1) + " x2 = " + str(self.x2)

class LineVertical():
    def __init__(self,x,y1,y2):
        self.x = x
        if y2>y1:
            self.y1 = y1
            self.y2 = y2
        else:
            self.y2 = y1
            self.y1 = y2
    def __str__(self):
        return "x = " + str(self.x) + " y1 = " + str(self.y1) + " y2 = " + str(self.y2)




if __name__ == "__main__":
    main()
