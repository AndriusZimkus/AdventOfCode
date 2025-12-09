def main():
      
    fileName = "test.txt"
    path = "../../../Advent Of Code Cases/2025/Day9/" + fileName

    points = []

    with open(path, 'r') as file:
        for line in file:
            curr = line.strip()
            point = list(map(int,curr.split(",")))
            points.append(point)

    print(len(points))
    #points.sort()
    for p in points:
        print(p)

if __name__ == "__main__":
    main()
