while True:
    noOfTestCasesString = input()
    noOfTestCases = int(noOfTestCasesString)
    if noOfTestCases < 1 or noOfTestCases > 31:
        print("Invalid Input")
    else:
        break
i = 0
while i < noOfTestCases:
    armtStrongNoString = input()
    armtStrongNo = int(armtStrongNoString)
    totalSum = 0
    if  armtStrongNo >= 100 and armtStrongNo < 1000:
        for c in armtStrongNoString:
            totalSum = totalSum + int(c) ** 3
        if totalSum == armtStrongNo:
            print("Yes")
        else:
            print("No")
    else:
        print("Invalid Input")
    i+=1

         
    