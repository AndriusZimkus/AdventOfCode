def main():
 
    fileName = "test.txt"
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
    total = 0
    for key in sets.keys():
        currentSet = sets[key]
        #print(currentSet)
        action = currentSet[len(currentSet)-1]
        #print(action)
        if action == '*':
            current = 1
        else:
            current = 0
        for i in range(len(currentSet)-1):
            if action == '*':
                current*=int(currentSet[i])
            else:
                current+=int(currentSet[i])

        #print (current)
        total += current

    print ("Total: ", total)

    with open(path, 'r') as file:
        sets = {}
        for line in file:
            print(list(line))

if __name__ == "__main__":
    main()
