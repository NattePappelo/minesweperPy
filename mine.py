"""
  __  __ _____ _   _ ______  _______          ________ _____  ______ _____  
 |  \/  |_   _| \ | |  ____|/ ____\ \        / /  ____|  __ \|  ____|  __ \ 
 | \  / | | | |  \| | |__  | (___  \ \  /\  / /| |__  | |__) | |__  | |__) |
 | |\/| | | | | . ` |  __|  \___ \  \ \/  \/ / |  __| |  ___/|  __| |  _  / 
 | |  | |_| |_| |\  | |____ ____) |  \  /\  /  | |____| |    | |____| | \ \ 
 |_|  |_|_____|_| \_|______|_____/    \/  \/   |______|_|    |______|_|  \_\ 
                                                                            

minesweper, a minesweeper game in pure python without liberaries by natte pappelo 2.5.2025 - 15.2.2026

"""




"""   SETTINGS   """

# the size of the playing grid
size = [10, 10]

# mine dencity  (higher number = less mines) (Needs to be an intager)
dencity = 4

# if the boxes should be extended to a square ratio
squareBoxes = True

# How a flag is shown in the grid
flagSign = "."

# How an undug square is shown in the grid
undugSign = " "

# How a dug square with no mines suorondig it is shown on the grid
zeroSign = "0"

# What character you add at the end of the input to flag instead of diging (cant be a letter used by the columns or rows)
flagChar = "."










# SETTINGS ERRORS

if type(size[0]) != type(3) or type(size[1]) != type(3):
    print("\nERROR: Size isnt intagers\n")
    input("press enter to close")
    exit()

if size[0] < 1 or size[1] < 1:
    print("\nERROR: Size too small\n")
    input("press enter to close")
    exit()

if size[0] > 26:
    print("\nERROR: Size too big. Currently Minesweper doesnt support a wider screen than to Z\n")
    input("press enter to close")
    exit()





# frågar efter seed
seed = input("Spam lite på tangetbole: ")


# RANDOM BOOLEAN GENERATOR
count = 0

def boolRandom():
    global seed
    global count
    count = count + 1

    return (hash(str(count) + str(seed)) // 10) % dencity == 0




# FUNCTON FOR PRINTING THE PLAYING FIELD
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
                    print(" " + flagSign + " |", end="")

                elif dug[y][x] and mineNums[y][x] == 0:
                    print(" "+ zeroSign +" |", end="")

                elif dug[y][x]:
                    print(" " + str(mineNums[y][x]) + " |", end="")
                else:
                    print(" " + undugSign + " |", end="")
            
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






columns = []
for i in range(size[0]):
    columns.append(chr(i + 97))



# FUNCTION FOR ASKING THE PLAYER WHAT THEY WANT TO DO
def question():

    global flags, flagCount, mines, dug


    inp = input('Van vill du gräv  (om du lägger "' + flagChar + '" i slute så flaggar du): ').lower()

    flag = flagChar.lower() in inp         # detect if the player wants to flag
    inp = inp.replace(flagChar.lower(), "")      # cleans away the flag char
    
    if inp[0] in columns:
        x = ord(inp[0]) - 97
        y = int(inp[1:]) - 1

    elif inp[-1] in columns:
        x = ord(inp[-1]) - 97
        y = int(inp[:-1]) - 1



    if flag:   # om spelaren vill flagga
        if flags[y][x]:   # om en flagga ska plockas bort
            flagCount -=1
        else:
            flagCount +=1
        flags[y][x] = not(flags[y][x])
        return None
    
    else: # om spelaren vill gräv
        return [y,x]




def placeMines():  # randomiserar ut minorna och lagar lite varierande variabler
    global mines, mineCount, mineNums, flags, dug

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



def main():
    global flagCount
    placeMines()  # görs endast så att printField() ska fungera, denna randomising körs över sedan
    printField()



    while 1:                     # fråga efter firstDig tills man får ett vättigt svar
        firstDig = question()
        if firstDig == None:
            print("Du måste gräva det första du gör")
        else:
            break




    # RANDOMISA UT MINORNA TILLS FIRSTDIG ÄR EN NOLLA

    isRandomising = True

    while isRandomising:

        placeMines()

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


        if mineNums[firstDig[0]][firstDig[1]] == 0:  # fortsätt randomisa tills firstDig är en nolla
            isRandomising = False



    dug[firstDig[0]][firstDig[1]] = True  # faktistk gräv firstDig




    flagCount = 0

    running = True
    stop = False
    victory = False

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
            return False

        elif victory:
            print("\n\nGONGRATULATIONS! YOU HAVE WON!!!!\n\n")
            return True

        

        

        dig = question()


        
        if dig != None:   # ifall inputten innehöll en gräv förfrågan

            
            if dug[dig[0]][dig[1]]:  # ifall man gräver en färdigt grävd ruta för att gräva grannarna


                x= dig[1]
                y= dig[0]


                # räknar hur många flaggor den valda rutan har runt sig
                neighourFlags = 0

                if y - 1 > -1 and x - 1 > -1 and flags[y-1][x-1]:    
                    neighourFlags += 1

                if y - 1 > -1 and flags[y-1][x]:
                    neighourFlags += 1

                if y - 1 > -1 and x + 1 < size[0] and flags[y-1][x+1]:
                    neighourFlags += 1

                if x - 1 > -1 and flags[y][x-1]:
                    neighourFlags += 1

                if x + 1 < size[0] and flags[y][x + 1]:
                    neighourFlags += 1

                if y + 1 < size[1] and x - 1 > -1 and flags[y + 1][x - 1]:
                    neighourFlags += 1

                if y + 1 < size[1] and flags[y + 1][x]:
                    neighourFlags += 1

                if x + 1 < size[0] and y + 1 < size[1] and flags[y + 1][x + 1]:
                    neighourFlags += 1



                # gräver grannarna om det finns rätt antal flaggor
                if neighourFlags == mineNums[y][x]: 
                    if y - 1 > -1 and x - 1 > -1 and (flags[y-1][x-1] == False):    
                        dug[y-1][x-1] = True
                        if mines[y-1][x-1]:
                                    stop = True
                            

                    if y - 1 > -1 and (flags[y-1][x] == False):
                        dug[y-1][x] = True
                        if mines[y-1][x]:
                                    stop = True

                    if y - 1 > -1 and x + 1 < size[0] and (flags[y-1][x+1] == False):
                        dug[y-1][x+1] = True
                        if mines[y-1][x+1]:
                            stop = True

                    if x - 1 > -1 and (flags[y][x-1] == False):
                        dug[y][x-1] = True
                        if mines[y][x-1]:
                            stop = True

                    if x + 1 < size[0] and (flags[y][x+1] == False):
                        dug[y][x+1] = True
                        if mines[y][x+1]:
                            stop = True

                    if y + 1 < size[1] and x - 1 > -1 and (flags[y+1][x-1] == False):
                        dug[y+1][x-1] = True
                        if mines[y+1][x-1]:
                            stop = True

                    if y + 1 < size[1] and (flags[y+1][x] == False):
                        dug[y+1][x] = True
                        if mines[y+1][x]:
                            stop = True

                    if x + 1 < size[0] and y + 1 < size[1] and (flags[y+1][x+1] == False):
                        dug[y+1][x+1] = True
                        if mines[y+1][x+1]:
                            stop = True



            else:
                dug[dig[0]][dig[1]] = True
                stop = mines[dig[0]][dig[1]]


            # CHECK FOR VICTORY
            victory = True
            for y in range(len(mines)):
                for x in range(len(mines[0])):
                    if not(dug[y][x] or mines[y][x]):
                        victory = False
                
                    



while 1:       
    main()

    if not(input("Do you want to play again (Y/N): ") in ["Y", "y"]):
        break

    print("\n")




