def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day8/" + fileName

    boxes = []
    groups = []

    if fileName == "test.txt":
        connections = 10
    else:
        connections = 1000
    top = 3
    
    with open(path, 'r') as file:
        i = 1
        for line in file:
            row = line.strip().split(',')
            currentBox = Box(int(row[0]),int(row[1]),int(row[2]),Group(i))
            boxes.append(currentBox)
            currentBox.group.boxes.append(currentBox)
            groups.append(currentBox.group)
            currentBox.group.count = 1
            i+=1
            
    distances = []

    #Slowest part - n**2 amount of distances
    for i in range(len(boxes)):
        for j in range(i+1,len(boxes)):
            distances.append(Distance(boxes[i],boxes[j]))

    sortedDistances = sorted(distances, key=lambda x: x.distance)

    for i in range(connections):
        currentDistance = sortedDistances[i]

        box1 = currentDistance.box1
        box2 = currentDistance.box2
        if box1.group != box2.group:
            bx2c = box2.group.count
            box2.group.count = 0
            for box in box2.group.boxes:
                box.group = box1.group
                box.group.boxes.append(box)
            box1.group.count += bx2c


    sortedGroups = sorted(groups, key=lambda x: x.count,reverse=True)


    product = 1
    for i in range(top):
        #print("Top ", i+1, sortedGroups[i].number)
        #print(sortedGroups[i].count)
        product *= sortedGroups[i].count

    print("Product: ",product)

    #print(len(sortedDistances))
    i = connections
    while True:

        currentDistance = sortedDistances[i]

        box1 = currentDistance.box1
        box2 = currentDistance.box2
        
        if box1.group != box2.group:
            bx2c = box2.group.count
            box2.group.count = 0
            for box in box2.group.boxes:
                box.group = box1.group
                box.group.boxes.append(box)
            box1.group.count += bx2c

        if box1.group.count == len(boxes):
            break
        i+=1

    print("Total connections: ", i)
    print("Last two box x coordinate product: ", box1.x*box2.x)
            

class Box():
    def __init__(self,x,y,z,group):
        self.x = x
        self.y = y
        self.z = z
        self.group = group

    def __str__(self):
        return f'x: {self.x}, y: {self.y}, z: {self.z}'

class Distance():
    def __init__(self,box1,box2):
        self.box1 = box1
        self.box2 = box2
        self.distance = (((box2.x - box1.x)**2)+\
                   ((box2.y - box1.y)**2)+\
                   ((box2.z - box1.z)**2))**(1/2)

class Group():
    def __init__(self,number):
        self.number = number
        self.boxes = []
        self.count = 0

if __name__ == "__main__":
    main()
