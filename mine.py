# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   __  __ _____ _   _ ______  _______          ________ _____  ______ _____    #
#  |  \/  |_   _| \ | |  ____|/ ____\ \        / /  ____|  __ \|  ____|  __ \   #
#  | \  / | | | |  \| | |__  | (___  \ \  /\  / /| |__  | |__) | |__  | |__) |  #
#  | |\/| | | | | . ` |  __|  \___ \  \ \/  \/ / |  __| |  ___/|  __| |  _  /   #
#  | |  | |_| |_| |\  | |____ ____) |  \  /\  /  | |____| |    | |____| | \ \   #
#  |_|  |_|_____|_| \_|______|_____/    \/  \/   |______|_|    |______|_|  \_\  #
#                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


                # # # # # # # # # # # # # # # # # # # # # # # # #
                #      A   B   C   D   E   F   G   H   I   J    #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  1 |   |   |   |   |   |   |   |   |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  2 |   |   |   |   |   |   |   |   |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  3 |   |   |   |   |   | 1 | 1 | 4 |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  4 |   |   |   |   | 2 | 1 | 0 | 2 | * |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  5 |   |   |   |   | 2 | 0 | 0 | 1 |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  6 |   | 2 | 2 | . | 2 | 0 | 0 | 1 |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  7 |   | 2 | 1 | 1 | 1 | 0 | 1 | 2 |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  8 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | . |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  9 | 0 | 0 | 0 | 1 | 1 | 2 | 2 |   |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                #  10| 0 | 0 | 0 | 1 |   |   |   |   |   |   |  #
                #    +---+---+---+---+---+---+---+---+---+---+  #
                # # # # # # # # # # # # # # # # # # # # # # # # #


"""
minesweper, a minesweeper game in pure python without liberaries by natte pappelo 2.5.2025 - 18.2.2026

Becouse of the limitation of no liberaries it needs to be terminal-based and cant have colors. Also the player
needs to give a seed to the randomizer by spamming the keyboard. 
"""





# # # # # # # # # # # # # # # # # # # # # # #
#    _________________________  ___________ #
#   / __/ __/_  __/_  __/  _/ |/ / ___/ __/ #    
#  _\ \/ _/  / /   / / _/ //    / (_ /\ \   #
# /___/___/ /_/   /_/ /___/_/|_/\___/___/   #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # #

# (SETTINGS)



# the size of the playing grid    [columns, rows]
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

# What character you add at the end of the input to flag instead of diging
# (cant be a character used by the columns or rows) (note that this isnt case sensitive)
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
    print("\nERROR: Size too big. (Currently Minesweper doesnt support a wider screen than to Z)\n")
    input("press enter to close")
    exit()





# Asks for a seed
seed = input("Spam some on the keyboard and press enter: ")


# RANDOM BOOLEAN GENERATOR
count = 0
def boolRandom():
    global seed, count
    count = count + 1
    return (hash(str(count) + str(seed)) // 10) % dencity == 0




# FUNCTON FOR PRINTING THE PLAYING FIELD
def printField():
    global squareBoxes, size, flags, dug, mineNums


    # prints the letters up at the top
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


    # Writes out the playing field
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
for i in range(size[0]):                # generates a list of all the column letters
    columns.append(chr(i + 97))



# FUNCTION FOR ASKING THE PLAYER WHAT THEY WANT TO DO
def question(withFlag=True):

    global flags, flagCount, mines, dug

    while 1:
        if withFlag:
            inp = input('Where do you want to dig?  (you flag by putting a "' + flagChar + '" at the end): ').lower()
        else:
            inp = input('Where do you want to dig?: ').lower()

        if len(inp) < len(str(size[1])) + 3 and len(inp) > 1:   # if the input has the correct lenght
            flag = flagChar.lower() in inp                      # detect if the player wants to flag
            inp = inp.replace(flagChar.lower(), "")             # cleans away the flag char
            
            if inp[0] in columns:                 # is the letter defining the column first
                x = ord(inp[0]) - 97
                try:
                    y = int(inp[1:]) - 1
                    if y >0 and y <=size[1]:
                        break
                except:
                    pass
                

            elif inp[-1] in columns:              # is the letter defining the column last
                x = ord(inp[-1]) - 97
                try:
                    y = int(inp[:-1]) - 1
                    if y >0 and y <=size[1]:
                        break
                except:
                    pass   
        

        print("ERROR: The input was not correctly entered")



    if flag:                # does the player want to flag
        if flags[y][x]:     # should a flag be removed instead of adding
            flagCount -=1
            flags[y][x] = False
        elif not(dug[y][x]):
            flagCount +=1
            flags[y][x] = True
        return None
    
    else: # if the player wants to dig
        return [y,x]




def placeMines():  # randomizes the mines and makes some wierd variables.
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
    placeMines()  # this is only done so printField() will work, this randomisation will be run over later.
    printField()

    flagCount = 0

    while 1:                     # asks for a first dig till the answer is alowed
        firstDig = question(False)
        if firstDig == None:
            printField()
            #print("Your first action must be a dig")
        else:
            break




    # RANDOMISES THE MINES TILL FIRSTDIG IS A ZERO

    while 1:

        placeMines()
        

        # calculates the numbers 
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


        if mineNums[firstDig[0]][firstDig[1]] == 0:  # loop if firstDig is a zero
            break



    dug[firstDig[0]][firstDig[1]] = True  # dig firstDig fr




    

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

                        
        print("mines left:", mineCount - flagCount)

        


        printField()



        if stop:
            print("\n\nGAME OVER!!!")
            return False

        elif victory:
            print("\n\nGONGRATULATIONS! YOU HAVE WON!!!!\n\n")
            return True

        

        

        dig = question()


        
        if dig != None:   # if the input consisted of a dig request

            if flags[dig[0]][dig[1]]:
                print("you tried to dig a flaged squere".upper())

            
            elif dug[dig[0]][dig[1]]:  # if the player digs an already dug squere to dig its neighbours


                x= dig[1]
                y= dig[0]


                # counts how many flags suround the selected squere
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



                # digs the neighbours if there is correct amount of flaged neighbours
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

