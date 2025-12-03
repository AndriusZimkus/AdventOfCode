def main():
 
    fileName = "input.txt"
    path = "../../../Advent Of Code Cases/2025/Day3/" + fileName

    banks = []
    
    with open(path, 'r') as file:
        for line in file:
            currentbank = list(line.strip())
            banks.append(list(map(int, currentbank)))

    totalJoltageTwo = 0

    for bank in banks:
        totalJoltageTwo += getBankJoltage(bank,2)

    print("Two joltage:",totalJoltageTwo)

    totalJoltageTwelve = 0

    for bank in banks:
        totalJoltageTwelve += getBankJoltage(bank,12)

    print("Twelve joltage:",totalJoltageTwelve)


def getBankJoltage(bank,digit):

    bankJoltage = 0
    
    while digit > 0:
        bank, jolt = getBankJoltageHelper(bank,digit)
        bankJoltage += jolt*(10**(digit-1))
        digit -= 1

    return bankJoltage

def getBankJoltageHelper(bank,digit):
    
    bankWithReserve = bank[0:len(bank)-(digit-1)]
    bankWithReserve.sort(reverse=True)
    jolt = bankWithReserve[0]
    indexFrom = bank.index(jolt)
    leftoverBank = bank[indexFrom+1:len(bank)]

    return leftoverBank, jolt
        
if __name__ == "__main__":
    main()
