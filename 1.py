from hashlib import new
import random

def getRandomArr(currentArr: list,quant: int, max: int, minV: int = 0):
    j = 0
    arr = []
    while j < quant:
        num = random.randint(minV,max)
        if currentArr is not None:
            if num in currentArr or num in arr:
                j-=1
            else:
                arr.append(num)
        elif num in arr:
            j-=1
        else:
            arr.append(num)
        j+=1
    return arr

def buildBinaryTree(arr, center: int = None):
    
    def addElems(index: int = -1):
        if index == -1:
            tree.append(-1)
            temp.append(-1)
        else:
            tree.append(arr[index])
            temp.append(index)

    def getCenter():
        cent = int(len(arr)/2)
        return cent

    def getPow():
        quantTreeElems = 0
        if center > len(arr)-center:
            quantTreeElems = center*2
        else:
            quantTreeElems = (len(arr)-center)*2

        pow = 0
        while 2**pow <= quantTreeElems:
            pow+=1
        pow -= 1
        return pow

    arr.sort()
    if center is None:
        center = getCenter()
    else:
        i = 0
        while True:
            if center == arr[i]:
                center = i
                break
            i+=1
    
    requiredPow = getPow()

    tree = []
    currentPow = 1
    prePreviousIndexes = [center]
    tree.append(arr[int(center)])
    if center == len(arr)-1:
        tree.append(arr[int(center/2)])
        tree.append(-1)
        previousIndexes = [int(center/2),-1]
    elif  center == 0:
        tree.append(-1)
        tree.append(arr[int((center+len(arr))/2)])
        previousIndexes = [-1,int((center+len(arr))/2)]
    else:
        tree.append(arr[int(center/2)])
        tree.append(arr[int((center+len(arr))/2)])
        previousIndexes = [int(center/2),int((center+len(arr))/2)]
    freeCell = -1
    while requiredPow > currentPow:
        temp = []
        for i in range(len(prePreviousIndexes)):
            for j in range(2):
                if previousIndexes[i*2+j] == freeCell:
                    addElems()
                else:
                    ind = previousIndexes[i*2+j]-int(abs(previousIndexes[i*2+j]-prePreviousIndexes[i])/2+0.5)
                    if ind < -1:
                        while ind < -1:
                            ind += 1
                    
                    if ind >= 0 and ind < len(arr):
                        if arr[ind] in tree:
                            if arr[ind+1] in tree:
                                addElems()
                            elif arr[ind+1] < previousIndexes[i*2+j]:
                                addElems(ind+1)
                            else:
                                addElems()
                        else:
                            addElems(ind)
                    elif ind+1 < previousIndexes[i*2+j] and arr[ind+1] not in tree:
                        addElems(ind+1)
                    else:
                        addElems()

                if previousIndexes[i*2+j] == freeCell:
                    addElems()
                else:
                    ind = previousIndexes[i*2+j]+int(abs(previousIndexes[i*2+j]-prePreviousIndexes[i])/2+0.5)
                    if ind > len(arr):
                        while ind > len(arr):
                            ind -= 1
                    
                    if ind >= 0 and ind < len(arr):
                        if arr[ind] in tree:
                            if arr[ind-1] in tree:
                                addElems()
                            elif arr[ind-1] > previousIndexes[i*2+j]:
                                addElems(ind-1)
                            else:
                                addElems()
                        else:
                            addElems(ind)
                    elif ind-1 > previousIndexes[i*2+j] and arr[ind-1] not in tree:
                        addElems(ind-1)
                    else:
                        addElems()
                    
        prePreviousIndexes.clear()
        for j in range(len(previousIndexes)):
            prePreviousIndexes.append(previousIndexes[j])
        previousIndexes.clear()
        for j in range(len(temp)):
            previousIndexes.append(temp[j])
        currentPow+=1

    return tree

def tryParseInt(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def askAboutCenter():
    center = None
    answer = input("Do you want to enter value of the root?(Y/N)")
    while True:
        if answer.lower() == "y":
            while True:
                num = input("Enter value of the root: ")
                num, result = tryParseInt(num)
                if result:
                    if num in arr:
                        center = num
                        break
                    else:
                        print("There is no such value in the array. Enter again.")
                else:
                    print("You entered not a integer number. Enter again.")
            break
        elif answer.lower() == "n":
            print("Value of the root is selected automatically")
            break
        else:
            print("You entered an incorrect value")
            answer = input("Entered value again.")
    return center

def checkInterval(quant,arr, max: int,min: int = 0):
    currentQuant = 0
    ran = max-min
    for i in range(len(arr)):
        if arr[i] <= max and arr[i] >= min:
            currentQuant+=1
    if quant <= ran - currentQuant+1:
        return True
    else:
        return False

def askAboutArr(currentArr: list = None):
    quant = 0
    while True:
        quant = input("Enter quantity of tree elements: ")
        quant, result = tryParseInt(quant)
        if result:
            break
        else:
            print("There is no the value in the array")

    answer = ""
    while True:
        answer = input("Generate an array automatically?(Y/N)")
        if answer.lower() == "y" or answer.lower() == "n":
            break
        else:
            print("You entered an incorrect value")

    arr = []
    if answer.lower() == "y":
        min = 0
        max = 0
        while True:
            min = input("Enter minimal value (must be >= 0): ")
            min, result = tryParseInt(min)
            if result:
                break
            elif not result:
                print("You entered not a integer number. Enter again.")
            elif min < 0:
                print("You entered a integer number less than 0. Enter again.")
        while True:
            max = input("Enter maximum value: ")
            max, result = tryParseInt(max)
            if result:
                if currentArr is not None:
                    interval = checkInterval(quant,currentArr,max,min)
                    if interval == False:
                        print("The generated numbers will be repeated in this interval")
                    else:
                        break
                else:
                    if max-min>=quant:
                        break   
                    else:
                        print("The generated numbers will be repeated in this interval")
            else:
                print("You entered not a integer number. Enter again.")
        arr = getRandomArr(currentArr,quant,max, min)
    else:
        print("Enter value:")
        i = 0
        while i<quant:
            num = input()
            num, result = tryParseInt(num)
            if result:
                if currentArr is not None:
                    if num in currentArr:
                        print("The number is already in the array, numbers cannot be repeated")
                    else:
                        i+=1
                        arr.append(num)
                else:
                    if num in arr:
                        print("The number is already in the array, numbers cannot be repeated")
                    else:
                        i+=1
                        arr.append(num)
            else:
                print("You entered not a integer number. Enter again.")

    return arr

def deleteValues(arr, value):
    i = 0
    while i < len(arr):
        if value == arr[i]:
            arr.pop(i)
            break
        i+=1
    return arr

def deleteBranch(tree, value: int):
    i = 0
    while i < len(tree):
        if value == tree[i]:
            break
        i+=1

    j = [i]
    newJ = []
    tree[i] = -1
    while True:
        if len(tree) > j[-1]*2:
            for index in range(len(j)):
                tree[j[index]*2 + 1] = -1
                tree[j[index]*2 + 2] = -1

                newJ.append(j[index]*2 + 1)
                newJ.append(j[index]*2 + 2)
            j.clear()
            for a in range(len(newJ)):
                j.append(newJ[a])
            newJ.clear()
        else:
            break
    return tree
                
def updateArr():
    arr.clear()
    for i in range(len(tree)):
        if tree[i] != -1:
            arr.append(tree[i])
    return arr

def printTreeLikeTree(tree):
    pow = 0
    while 2**pow <= len(tree):
        pow+=1
    pow -= 1

    currentPow = 0
    printedElemsIndexNum = 0
    toFile = str(tree)+"\n"
    while currentPow <= pow:
        print("\n level" + str(currentPow) +"  :",end="")
        toFile+="\n level" + str(currentPow) +"  :" 
        for i in range(2**currentPow):
            if (printedElemsIndexNum+i) == 2**currentPow-1 or (printedElemsIndexNum+i) == 0:
                for j in range(int(2**pow/2**currentPow)):
                    toFile+="\t"
                    print("\t",end="")
                toFile+=str(tree[printedElemsIndexNum+i])
                print(tree[printedElemsIndexNum+i],end="")
            else:
                for j in range(int(2**pow/2**(currentPow-1))):
                    toFile+="\t"
                    print("\t",end="")
                toFile+=str(tree[printedElemsIndexNum+i])   
                print(tree[printedElemsIndexNum+i],end="")
        printedElemsIndexNum+=2**currentPow
        currentPow+=1
    return toFile

def writeToFile(toFile):
    file = open("tree.txt", "a")
    file.write("\n\n----------------------------------------------------------------------------------------------------\n\n"+toFile)
    file.close()

if __name__ == "__main__":
    toFile = ""
    arr = askAboutArr()
    print(arr)
    center = askAboutCenter()
    tree = buildBinaryTree(arr, center)
    print(tree)
    toFile = printTreeLikeTree(tree)
    writeToFile(toFile)

    while True:
        action = input("\nSelect next action: addition(add), removal(rem), root change(chr), tree rebuild(reb), exit(e)\n")
        if action.lower() == "add":
            addToArr = askAboutArr(arr)
            print(addToArr)
            for i in range(len(addToArr)):
                arr.append(addToArr[i])
            print(arr)
            center = askAboutCenter()
            tree = buildBinaryTree(arr, center)
        elif action.lower() == "rem":
            answer = ""
            while True:
                answer = input("Remove one value(1) or the whole branch(2)?\n")
                if answer == "1" or answer == "2":
                    break
                else:
                    print("You entered an incorrect value. Enter 1 or 2\n")
            if answer == "1":
                value = 0
                while True:
                    value = input("Enter value for removal: ")
                    value, result = tryParseInt(value)
                    if result:
                        if value in arr:
                            break
                        else:
                            print("There is no the value in the array")
                    else:
                        print("There is no the value in the array")
                arr = deleteValues(arr,value)
                print(arr)
                tree = buildBinaryTree(arr)
            if answer == "2":
                while True:
                    value = input("Enter value for removal: ")
                    value, result = tryParseInt(value)
                    if result:
                        if value in arr:
                            break
                        else:
                            print("There is no the value in the array")
                    else:
                        print("You entered not a integer number. Enter again.")
                tree = deleteBranch(tree, value)            
                arr = updateArr()

        elif action.lower() == "chr":        
            center = askAboutCenter()
            print(arr)
            tree = buildBinaryTree(arr, center)
        elif action.lower() == "reb":
            print(arr)
            tree = buildBinaryTree(arr)
        elif action.lower() == "e":
            break
        else:
            action = input("\nYou entered an incorrect value. \nSelect next action: addition(add), removal(rem), root change(chr), tree rebuild(reb), exit(e)\n")
        print(tree)
        toFile = printTreeLikeTree(tree)
        writeToFile(toFile)

