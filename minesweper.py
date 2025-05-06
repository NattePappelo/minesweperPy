"""
minesweper without liberaries by natte pappelo 2.5.2025 - 5.5.2025
"""

# the size of the playing grid
size = [10, 10]

# mine dencity  (higher number = less mines)
dencity = 4

# if the boxes should be extended to a square ratio
squareBoxes = True









# frågar efter seed
seed = hash(input("Spam lite på tangetbole: "))






count = 0

def boolRandom():
    global seed
    global count
    count = count + 1

    return hash(str(count) + str(seed)) % dencity == 0













def printField():
    global squareBoxes, size, flags, dug, mineNums



    # prints the lethers up at the top
    if squareBoxes:
        print("    ", end="")
    else:
        print("   ", end="")
    
    for i in range(size[0]):
        if squareBoxes:
            print(str(chr(i + 65)) + "   ", end="")
        else:
            print(str(chr(i + 65)) + " ", end="")
    print()




    # prints the line at the top
    print("  +", end="")

    for i in range(size[0]):
        if squareBoxes:
            print("---+", end="")
        else:
            print("-+", end="")
    print()



    # skriver ut spelfältet
    for y in range(size[1]):
        if y + 1 < 10:
            print(str(y + 1) + " |", end="")
        else:
            print(str(y + 1) + "|", end="")

        for x in range(size[0]):
            if squareBoxes:
                if flags[y][x]:
                    print(" f |", end="")

                elif dug[y][x] and mineNums[y][x] == 0:
                    print("   |", end="")

                elif dug[y][x]:
                    print(" " + str(mineNums[y][x]) + " |", end="")
                else:
                    print(" # |", end="")
            
            else:
                if flags[y][x]:
                    print("f|", end="")

                elif dug[y][x]:
                    print(str(mineNums[y][x]) + "|", end="")
                else:
                    print(" |", end="")

        print()

        print("  +", end="")
        for i in range(size[0]):
            if squareBoxes:
                print("---+", end="")
            else:
                print("-+", end="")
        print()

    print()










def question():

    global flags, flagCount, size, mines, dug


    inp = input('Van vill du gräv  (om du lägger "f" i slute så flaggar du): ').lower()

    if len(inp) == 3 and inp[2] == "f" and not(dug[int(inp[1]) - 1][ord(inp[0]) - 97]):
        if flags[int(inp[1]) - 1][ord(inp[0]) - 97]:
            flagCount -= 1
        else:
            flagCount += 1

        flags[int(inp[1]) - 1][ord(inp[0]) - 97] = not(flags[int(inp[1]) - 1][ord(inp[0]) - 97])
        return None

    elif len(inp) == 4 and size[0] > 9 and inp[3] == "f":
        if flags[int(inp[1] + inp[2]) - 1][ord(inp[0]) - 97]:
            flagCount -= 1
        else:
            flagCount += 1

        flags[int(inp[1] + inp[2]) - 1][ord(inp[0]) - 97] = not(flags[int(inp[1] + inp[2]) - 1][ord(inp[0]) - 97])
        return None



    elif len(inp) == 2:
        if flags[int(inp[1]) - 1][ord(inp[0]) - 97]:
            print("hödu! hanje e flagga")
            return None

        else:
            return [int(inp[1]) - 1, ord(inp[0]) - 97]
            
                

    elif len(inp) == 3 and size[0] > 9:
        if flags[int(inp[1] + inp[2]) - 1][ord(inp[0]) - 97]:
            print("hödu! hanje e flagga")
            return None

        else:
            return [int(inp[1] + inp[2]) - 1, ord(inp[0]) - 97]
            

    elif inp == "stop" or inp == "exit":
        exit()

    else:
        print("\n\n\nVa fan skrev du!?!?!?!?!?!?!?!?\n\n\n")











# randomiserar ut minorna och lagar lite varierande variabler
mines = []
mineCount = 0
mineNums = []
flags = []  # if a space has a flag
dug = []  # if a space is revealed


for y in range(size[1]):
    mines.append([])
    mineNums.append([])
    flags.append([])
    dug.append([])
    for x in range(size[0]):
        mineNums[y].append("*")
        flags[y].append(False)
        dug[y].append(False)

        mines[y].append(int(boolRandom()))

        if mines[y][-1] == 1:
            mineCount += 1




printField()

idiot = 1

while idiot:
    firstDig = question()
    if firstDig == None:
        print("du e en idiot")
    else:
        idiot = 0






isRandomising = True


while isRandomising:

    # randomiserar ut minorna och lagar lite varierande variabler
    mines = []
    mineCount = 0
    mineNums = []
    flags = []  # if a space has a flag
    dug = []  # if a space is revealed


    for y in range(size[1]):
        mines.append([])
        mineNums.append([])
        flags.append([])
        dug.append([])
        for x in range(size[0]):
            mineNums[y].append("*")
            flags[y].append(False)
            dug[y].append(False)

            mines[y].append(int(boolRandom()))

            if mines[y][-1] == 1:
                mineCount += 1


    # print(mines)


    # kalkylerar siffrorna

    for y in range(len(mines)):
        for x in range(len(mines[0])):
            if mines[y][x] == 0:
                mineNums[y][x] = 0

                if y - 1 > -1 and x - 1 > -1:
                    mineNums[y][x] = mineNums[y][x] + mines[y - 1][x - 1]

                if y - 1 > -1:
                    mineNums[y][x] = mineNums[y][x] + mines[y - 1][x]

                if y - 1 > -1 and x + 1 < size[0]:
                    mineNums[y][x] = mineNums[y][x] + mines[y - 1][x + 1]

                if x - 1 > -1:
                    mineNums[y][x] = mineNums[y][x] + mines[y][x - 1]

                if x + 1 < size[0]:
                    mineNums[y][x] = mineNums[y][x] + mines[y][x + 1]

                if y + 1 < size[1] and x - 1 > -1:
                    mineNums[y][x] = mineNums[y][x] + mines[y + 1][x - 1]

                if y + 1 < size[1]:
                    mineNums[y][x] = mineNums[y][x] + mines[y + 1][x]

                if x + 1 < size[0] and y + 1 < size[1]:
                    mineNums[y][x] = mineNums[y][x] + mines[y + 1][x + 1]

    if mineNums[firstDig[0]][firstDig[1]] == 0:
        isRandomising = False






dug[firstDig[0]][firstDig[1]] = True










flagCount = 0

running = True
stop = False

while running:

    checkingZeros = True
    
    while checkingZeros:

        checkingZeros = False


        for y in range(len(mineNums)):
            for x in range(len(mineNums[y])):

                if dug[y][x] and mineNums[y][x] == 0:

                    if y - 1 > -1 and x - 1 > -1 and not(dug[y - 1][x - 1]):    
                        checkingZeros = True
                        dug[y - 1][x - 1] = True

                    if y - 1 > -1 and not(dug[y - 1][x]):
                        checkingZeros = True
                        dug[y - 1][x] = True

                    if y - 1 > -1 and x + 1 < size[0] and not(dug[y - 1][x + 1]):
                        checkingZeros = True
                        dug[y - 1][x + 1] = True

                    if x - 1 > -1 and not(dug[y][x - 1]):
                        checkingZeros = True
                        dug[y][x - 1] = True

                    if x + 1 < size[0] and not(dug[y][x + 1]):
                        checkingZeros = True
                        dug[y][x + 1] = True

                    if y + 1 < size[1] and x - 1 > -1 and not(dug[y + 1][x - 1]):
                        checkingZeros = True
                        dug[y + 1][x - 1] = True

                    if y + 1 < size[1] and not(dug[y + 1][x]):
                        checkingZeros = True
                        dug[y + 1][x] = True

                    if x + 1 < size[0] and y + 1 < size[1] and not(dug[y + 1][x + 1]):
                        checkingZeros = True
                        dug[y + 1][x + 1] = True

                    
    print("antal minor kvar:", mineCount - flagCount)

    


    printField()



    if stop:
        print("\n\nGAME OVER!!!")
        break

    

    

    dig = question()


    if dig != None:
        dug[dig[0]][dig[1]] = True
        stop = mines[dig[0]][dig[1]]
            





running = False
print()


input()
