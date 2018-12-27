import math
while True:
    noOfTestCasesString = input()
    noOfTestCases = int(noOfTestCasesString)
    if noOfTestCases < 1 or noOfTestCases > 200:
        print("Invalid Input")
    else:
        break
i = 0
while i < noOfTestCases:
    armtStrongNoString = input()
    armtStrongNo = int(armtStrongNoString)
    totalSum = 0
    if  armtStrongNo >= 1 and armtStrongNo < 1000:
        for c in armtStrongNoString:
            totalSum = totalSum + int(c)
        totatlSumString = str(totalSum)
        lastIndex = len(totatlSumString)-1
        sumPalin=True
        
        if(lastIndex <3):
            for ind,c in enumerate(totatlSumString):
                if(totatlSumString[ind] != totatlSumString[lastIndex-ind]):
                    sumPalin =False
                    break
        else:
            for ind, c in zip(range(math.floor(lastIndex/2)), totatlSumString):
                if(totatlSumString[ind] != totatlSumString[lastIndex-ind]):
                    sumPalin =False
                    break

        print("YES") if sumPalin else print("NO")
    else:
        print("Invalid Input")
    i+=1

         
    
