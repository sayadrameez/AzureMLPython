while True:
    noOfTestCasesString = input()
    noOfTestCases = int(noOfTestCasesString)
    if noOfTestCases < 1 or noOfTestCases > 100:
        print("Invalid Input")
    else:
        break
i = 0

while i < noOfTestCases:
    armtStrongNoString = input()
    #armtStrongNo = int(armtStrongNoString)
    if  len(armtStrongNoString) >= 1 and len(armtStrongNoString) <= 16:
        try:
            print(int(armtStrongNoString,2))
        except:
            print("Invalid Input")
    else:
        print("Invalid Input")
    i+=1