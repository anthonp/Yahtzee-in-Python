# Anthony 
# COMP-150
# Yahtzee Game Final Project
# 12/13/2021

# Prerequisites:
#     
#    * 'cImage.py' must be in the same directory as 'anthonys_yahtzee.py'
#    * 'dice.gif' must be in the same directory as 'anthonys_yahtzee.py'
#    * Save files are created automatically upon saving the game at the end.
#    * User cannot load a previous game if there are no saves.

# Running:
#
#    * Upon start up, game runs automatically.
#    * If user stops game, it can be started with 'startGame()'
#    * When running the game, click within the window of the graphical
#     dice to CLOSE or else program will hang if you press the red "X".

import random
from random import randint
#from cImage import *

# Core User section:--------------------------------------------

# startGame() starts a completely fresh game.
# The dictionary returns items as you play the game.
def startGame():
        print("anthonp, 2021")
        print("\nWould you like to load from an existing game?")
        print("'n' starts new game, 'y' loads existing game.\n")
        userPrompt = input("Enter 'y' or 'n': ")
        # Main while loop to wash user input as the main while loop.
        while userPrompt.lower() != 'y' and userPrompt.lower() != 'n':
                print("\nIncorrect response...\n")
                startGame()
        if userPrompt.lower() == 'y':
                loadAGame() # load current saved game
                scoreChart()
                startRound()
        if userPrompt.lower() == 'n':
                scoreChart()
                startRound()

# Called function which only just starts a new round:
def startRound():
        game(upperScore, lowerScore, sortedDice, usedSlots)

# Called function which asks if user wants another round:
def continueGame():
        print("\nWould you like to play another round?\n")
        nextRound = input("Enter 'y' or 'n': ")
        # While loops sanitize user input:
        while nextRound.lower() != 'y' and nextRound.lower() != 'n':
                print("\nIncorrect response...")
                continueGame()
        if nextRound.lower() == 'y':
                startRound()
        if nextRound.lower() == 'n':
                endGame()

# endGame() calculates score and saves game data to a text file
def endGame():
        print("The total score for you is: " + str(totalling()))
        print("Upper Score: " + ''.join(str(upperScore)))
        print("Lower Score: " + ''.join(str(lowerScore)))
        print("\nWould you like to save your game?\n")
        userIn = input("Enter 'y' or 'n': ")
        while userIn.lower() != 'y' and userIn.lower() != 'n':
                print("\nIncorrect response...\n")
                # calling end game function
                endGame()
        if userIn.lower() == 'y':
                # calling write to file function
                writeToFile()
                print("Re-run program to start again...")
        if userIn.lower() == 'n':
                startGame()

# Initialization Section:----------------------------------

# User Note:
#-------------------------------------------------------------------------
# * I chose to use global variables because they are easier to access
# * With this in mind, I take the proper precautions in handling 
#       global variables.
#-------------------------------------------------------------------------

# Yahtzee tally:
# Keeps track of total yahtzees for bonus calculation
yahtzeeTally = []

# Initialized dice list used throughout game
sortedDice = [0, 0, 0, 0, 0]

# List of unused scores; storage list
slotsLeft = []

# Upper and Lower scores; last upper position holds 35 pt bonus
upperScore = [0, 0, 0, 0, 0, 0, 0] # index 0-5, but values 1-6;
lowerScore = [0, 0, 0, 0, 0, 0, 0, 0] # indices for lower scores

# Used/unused slots as dictionary:
# True and False are boolean and must be treated as such
usedSlots = {"1's":False, "2's":False, "3's":False,
             "4's":False, "5's":False, "6's":False,
             "bonus_yahtzee":False, "3_of_a_kind":False,
             "4_of_a_kind":False, "full_house":False,
             "small_straight":False, "large_straight":False,
             "yahtzee":False, "chance":False}

# Save/Loading Section:-------------------------------------

# Function that writes to a textfile given global variables:
# Yahtzee, slotsLeft, upperScore, lowerScore, usedSlots
def writeToFile():
        # Writing functions which write to txt files:
        #     * Could have been made to be reusable, 
        #       but involves too much risk with unique data.
        with open("anthony_yahtzee_save_tally.txt", mode="w") as txt:
                for y in yahtzeeTally:
                        txt.write(str(y) +"\n")

        with open("anthony_yahtzee_save_slots_left.txt", mode="w") as txt:
                for s in slotsLeft:
                        txt.write(str(s) +"\n")

        with open("anthony_yahtzee_save_upper.txt", mode="w") as txt:
                for u in upperScore:
                        txt.write(str(u) +"\n")

        with open("anthony_yahtzee_save_lower.txt", mode="w") as txt:
                for l in lowerScore:
                        txt.write(str(l) +"\n")

        with open("anthony_yahtzee_save_used_slots.txt", mode="w") as txt:
                for i in usedSlots:
                    txt.write(str(i) + " " + str(usedSlots[i]) + '\n')

# Called Function which loads to global variables from text files:
# Yahtzee, slotsLeft, upperScore, lowerScore, usedSlots
def loadAGame():
        # Clear all populated lists:
        yahtzeeTally.clear()
        slotsLeft.clear()
        upperScore.clear()
        lowerScore.clear()

        # Opening each save file 
        with open("anthony_yahtzee_save_tally.txt", "r") as saveFile:
                for line in saveFile:
                        # appending to lists
                        yahtzeeTally.append(int(line.strip()))

        with open("anthony_yahtzee_save_slots_left.txt", "r") as saveFile:
                for line in saveFile:
                        slotsLeft.append(int(line.strip()))

        with open("anthony_yahtzee_save_upper.txt", "r") as saveFile:
                for line in saveFile:
                        upperScore.append(int(line.strip()))

        with open("anthony_yahtzee_save_lower.txt", "r") as saveFile:
                for line in saveFile:
                        lowerScore.append(int(line.strip()))

        # usedSlots dictionary conversion which reads str to bool:
        with open("anthony_yahtzee_save_used_slots.txt") as saveFile:
            for line in saveFile:
                (key, value) = line.split()
                # If conditionals which ask if string == True or == False
                if value == 'True':
                        # assigns bool true if string 'True'
                    value = True
                    usedSlots[key] = value
                elif value == 'False':
                    value = False
                    usedSlots[key] = value
                else:
                    raise ValueError
        return yahtzeeTally, slotsLeft, upperScore, lowerScore, usedSlots

# Core Components:-----------------------------------------

# Called at the end of a round and beginning of a game to display scores loaded
def scoreChart():
        print("Upper Scores:")
        # Upper list names
        upperList = ["One's: ", "Two's: ", "Three's: ",
                     "Four's: ", "Five's: ", "Six's: ",
                     "Upper Bonus: "]

        # Printing upperscore alongside list of names:
        lowerY = 0
        for i in upperScore:
                print(str(upperList[lowerY]) + " " + str(i))
                lowerY += 1
        print("Upper Total: " + str(sum(upperScore)))

        print("\nLower Scores:")
        # Lower list names
        lowerList = ["3 of a kind: ", "4 of a kind: ",
                     "Full House: ", "Small Straight: ",
                     "Large Straight: ", "Yahtzees: ",
                     "Chance: ", "Yahtzee Bonus: "]

        # Printing lowerScore alongside list of names:
        lowerX = 0
        for i in lowerScore:
                print(str(lowerList[lowerX]) + " " + str(i))
                lowerX += 1
        print(str("Yahtzees so far: " + str("".join(str(yahtzeeTally)))))
        print("Lower Total: " + str(sum(lowerScore)))
        print("\nCombined Total: " + str(totalling()))

# # Graphical dice call which handles displaying of the dice
# def graphicalDice(imageFile, sortedDice):
#         passedImage = FileImage(imageFile)
#         width = passedImage.getWidth()
#         height = passedImage.getHeight()

#         windowHeader = ImageWin("Your Currently Held Roll", 580, height)
#         canvas = EmptyImage(580, height)

#         z = 0
#         for die in sortedDice:
#                 # Math that determines beginning position of img:
#                 beginMath = (die - 1)  * 116
#                 for diceWidth in range(beginMath, beginMath + (116) - 1):
#                         for diceHeight in range(0, height - 1):
#                                 alterPixel = passedImage.getPixel(diceWidth, diceHeight)
#                                 canvas.setPixel(diceWidth - beginMath + (z * 116), diceHeight,
#                                                 alterPixel)
                
#                 # increment z after every die in sortedDice:
#                 z += 1
#         canvas.draw(windowHeader)
#         windowHeader.exitOnClick()

# Rolling of the dice; appends to global sortedDice list:
def rollingAction():
    # Clears any prior dice: 
    sortedDice.clear()
    for d in range(5):
        sortedDice.append(randint(1,6))
    return sortedDice.sort()

# Change of the dice by user:
def roll():
    # Calls each die function in order
    diceOne()
    diceTwo()
    diceThree()
    diceFour()
    diceFive()
    # Returns a list of sorted dice:
    return sortedDice.sort()

# Used for new scoring system:
def getDieInput(param):
    posInput = input(param)
    return posInput

# Core Mathematics:----------------------------------------

# Check for 3 of a kind:
def checkThreeKind(sortedDice):
        if sortedDice[0] == sortedDice[2]:
                return True
        if sortedDice[1] == sortedDice[3]:
                return True
        if sortedDice[2] == sortedDice[4]:
                return True
        else:
                return False

# Check for 4 of a kind:
def checkFourKind(sortedDice):
        if sortedDice[0] == sortedDice[3]:
                return True
        if sortedDice[1] == sortedDice[4]:
                return True
        else:
                return False

# Check for full house:
def checkFullHouse(sortedDice):
        if sortedDice[0] == sortedDice[2] and sortedDice[3] == sortedDice[4]:
                return True
        if sortedDice[0] == sortedDice[1] and sortedDice[2] == sortedDice[4]:
                return True
        else:
                return False

# Check for small straight:
def checkSmallStraight(sortedDice):
        myRoll = sortedDice[:]
        # I got this idea "fromkeys" from
        # w3schools.com
        myRoll = list(dict.fromkeys(myRoll))
        patternOne = [1, 2, 3, 4]
        patternTwo = [2, 3, 4, 5]
        patternThree = [3, 4, 5, 6]
        # using all() function
        if(all(i in myRoll for i in patternOne)): # w3schools.com
            return True
        if(all(i in myRoll for i in patternTwo)): # w3schools.com
            return True
        if(all(i in myRoll for i in patternThree)): # w3schools.com
            return True
        else:
            return False

# Check for large straight:
def checkLargeStraight(sortedDice):
        if sortedDice == [1, 2, 3, 4, 5]:
                return True
        if sortedDice == [2, 3, 4, 5, 6]:
                return True
        else:
                return False

# Check for a yahtzee:
def checkYahtzee(sortedDice):
        if sortedDice[0] == sortedDice[4]:
                return True
        else:
                return False

# Calculate chance
def calculateChance(sortedDice):
        lowerScore[6] = sum(sortedDice)
        return lowerScore

# Check for upper bonus:
def upperBonus(upperScore):
        if sum(upperScore) >= 63:
                upperScore[6] = 35
                return True
        else:
                upperScore[6] = 0
                return False
        return upperScore

# Calculate if yahtzee bonus is true:
def calculateIfYahtzeeBonus():
        if sum(yahtzeeTally) > 1:
                yahtzeeBonus = (sum(yahtzeeTally) - 1) * 50
                lowerScore[7] = yahtzeeBonus
                return True
        else:
                return False

# Total all points in lists:
def totalling():
        # Totalling upper bonus separately not required
        return sum(upperScore) + sum(lowerScore)

# Gameplay Functionality:--------------------------------------

# Function to hold our scoring key:
def scoringKey():
        # Condensed for readability in code:
        print("Scoring Key:\n------------------\nEnter 1 for 1's")
        print("Enter 2 for 2's\nEnter 3 for 3's\nEnter 4 for 4's")
        print("Enter 5 for 5's\nEnter 6 for 6's\n------------------")
        print("Enter 7 for 3 of a kind\nEnter 8 for 4 of a kind")
        print("Enter 9 for full house\nEnter 10 for small straight")
        print("Enter 11 for large straight\nEnter 12 for yahtzee")
        print("Enter 13 for chance\n------------------\n\nSlots Left:")
        # slots left which loops through and prints each unused slot:
        slotsLeft = [slot for slot, value in usedSlots.items() if value
                     == False]
        for i in slotsLeft:
              print(i + "")
        print("\nWhichever is selected will be checked\n------------------")

# Dice calls:
def diceOne():
    print("\nWould you like to keep dice #1? ")
    pos1 = getDieInput("Enter 'y' or 'n': ")
    # sanitizeUserInput() serves to sanitize the
    # input from users that might be malformed.
    sanitizeUserInput(pos1, 1, diceOne)
def diceTwo():
    print("\nWould you like to keep dice #2? ")
    pos2 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos2, 2, diceTwo)
def diceThree():
    print("\nWould you like to keep dice #3? ")
    pos3 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos3, 3, diceThree)
def diceFour():
    print("\nWould you like to keep dice #4? ")
    pos4 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos4, 4, diceFour)
def diceFive():
    print("\nWould you like to keep dice #5? ")
    pos5 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos5, 5, diceFive)
    return sortedDice.sort()
    
# Sanitize User Input for dice rolls:
def sanitizeUserInput(stringInput, number, dice):
    if (str(stringInput)).lower() == 'y':
        #print("Keeping #" + str(number) + "...\n")
        return #sortedDice.sort()
    if (str(stringInput)).lower() == 'n':
        sortedDice[int(number) - 1] = (randint(1,6))
        #print("Updated\n")
        return #sortedDice.sort()
    if (str(stringInput)).lower() != "n" or "y":
        print("\ninvalid entry...")
        dice()

# Core game function:
def game(upperScore, lowerScore, sortedDice, usedSlots):
        print("\nROLL ONE:")
        print("Rolling...\nDumping cup...\n")
        rollingAction() # First roll.
        print("Current Roll: " + str(sortedDice[0]) + ", "
          + str(sortedDice[1]) + ", " +
          str(sortedDice[2]) + ", " +
          str(sortedDice[3]) + ", "
          + str(sortedDice[4]))
        
        # Calling graphical dice for roll #1:
        #graphicalDice('dice.gif', sortedDice)
        # Asking if user wants a second roll:
        print("Would you like a SECOND ROLL? ")
        # Roll two determination function
        rollTwo = getDieInput("Enter 'y' or 'n': ")
        if (str(rollTwo)).lower() == "y":
                print("\nROLL TWO:")
                roll() # Second roll.
                print("\nYour dice so far: " + str(sortedDice[0])
                      + ", " + str(sortedDice[1]) + ", "
                      + str(sortedDice[2]) + ", "+ str(sortedDice[3])
                      + ", " + str(sortedDice[4]) + "\n")
        elif (str(rollTwo)).lower() == "n":
                print("")
                print("Current dice: " + str(sortedDice[0]) + ", "
                      + str(sortedDice[1]) + ", " + str(sortedDice[2]) + ", "
                      + str(sortedDice[3]) + ", " + str(sortedDice[4]) + "\n")
        else:
                print("\n\nError with your input, restarting\n")
                startGame()
                return
        
        # Call graphical dice function for roll #2:
        #graphicalDice('dice.gif', sortedDice)

        # Asking if user wants a third roll:
        print("Would you like your THIRD ROLL? ")

        # Roll three determination function
        rollThree = getDieInput("Enter 'y' or 'n': ")
        if (str(rollThree)).lower() == "y":
                print("\nROLL THREE:")
                roll() # Third roll.
                print("\nYour dice so far: " + str(sortedDice[0])
                      + ", " + str(sortedDice[1]) + ", "
                      + str(sortedDice[2]) + ", "+ str(sortedDice[3])
                      + ", " + str(sortedDice[4]) + "\n")
        elif (str(rollThree)).lower() == "n":
                print("")
                print("Current dice: " + str(sortedDice[0]) + ", "
                      + str(sortedDice[1]) + ", " + str(sortedDice[2]) + ", "
                      + str(sortedDice[3]) + ", " + str(sortedDice[4]) + "\n")
        else:
                print("\n\nError with your input, restarting\n")
                startGame()
                return
        
        # Calling graphical dice for roll #3
        #graphicalDice('dice.gif', sortedDice)

        # Calling the score sheet:
        scoringKey()
        print("How do you want to score " + str(sortedDice[0]) + ", "
              + str(sortedDice[1]) + ", " +
              str(sortedDice[2]) + ", " + str(sortedDice[3])
              + ", " + str(sortedDice[4]) + "?")
        whereToScore = getDieInput("Enter a number: ")

        # If statements ask where to score based on input
        if whereToScore.isalpha(): # "Is input a letter/string"
                print("\nYou entered a string, not a number\n")
                print("Restarting Game...\n")
                startRound()
                return
        # Where to score based on input:
        # (This pattern repeats for the rest of the scoring)
        if int(whereToScore) == 1:
                # If dictionary slot is false, and there is a 1 in dice roll:
                if usedSlots["1's"] == False and 1 in sortedDice:
                        # Set the score via index to the value of count
                        upperScore[0] = sortedDice.count(1)
                        usedSlots["1's"] = True
                        print("\n...Success!\n")
                else:
                        # Don't score, because dice are full/no match
                        print("1's are full/dice don't match\n")
        if int(whereToScore) == 2:
                if usedSlots["2's"] == False and 2 in sortedDice:
                        upperScore[1] = sortedDice.count(2)*2
                        usedSlots["2's"] = True
                        print("\n...Success!\n")
                else:
                        print("2's are full/dice don't match\n")
        if int(whereToScore) == 3:
                if usedSlots["3's"] == False and 3 in sortedDice:
                        upperScore[2] = sortedDice.count(3)*3
                        usedSlots["3's"] = True
                        print("\n...Success!\n")
                else:
                        print("3's are full/dice don't match\n")
        if int(whereToScore) == 4:
                if usedSlots["4's"] == False and 4 in sortedDice:
                        upperScore[3] = sortedDice.count(4)*4
                        usedSlots["4's"] = True
                        print("\n...Success!\n")
                else:
                        print("4's are full/dice don't match\n")
        if int(whereToScore) == 5:
                if usedSlots["5's"] == False and 5 in sortedDice:
                        upperScore[4] = sortedDice.count(5)*5
                        usedSlots["5's"] = True
                        print("\n...Success!\n")
                else:
                        print("5's are full/dice don't match")
                        print("")
        if int(whereToScore) == 6:
                if usedSlots["6's"] == False and 6 in sortedDice:
                        upperScore[5] = sortedDice.count(6)*6
                        usedSlots["6's"] = True
                        print("\n...Success!\n")
                else:
                        print("6's are full/dice don't match\n")
        if int(whereToScore) == 7:
                if checkThreeKind(sortedDice) and usedSlots["3_of_a_kind"] == False:
                        lowerScore[0] = sum(sortedDice)
                        usedSlots["3_of_a_kind"] = True
                        print("\n...Success!\n")
                else:
                        print("3 of a kind full/no match\n")
        if int(whereToScore) == 8:
                if checkFourKind(sortedDice) and usedSlots["4_of_a_kind"] == False:
                        lowerScore[1] = sum(sortedDice)
                        usedSlots["4_of_a_kind"] = True
                        print("\n...Success!\n")
                else:
                        print("4 of a kind full/no match\n")
        if int(whereToScore) == 9:
                if checkFullHouse(sortedDice) and usedSlots["full_house"] == False:
                        lowerScore[2] = 25
                        usedSlots["full_house"] = True
                        print("\n...Success!\n")
                else:
                        print("full house full/no match\n")
        if int(whereToScore) == 10:
                if checkSmallStraight(sortedDice) and usedSlots["small_straight"] == False:
                        lowerScore[3] = 30
                        usedSlots["small_straight"] = True
                        print("\n...Success!\n")
                else:
                        print("small straight full/no match\n")
        if int(whereToScore) == 11:
                if checkLargeStraight(sortedDice) and usedSlots["large_straight"] == False:
                        lowerScore[4] = 40
                        usedSlots["large_straight"] = True
                        print("\n...Success!\n")
                else:
                        print("large straight full/no match\n")
        if int(whereToScore) == 12:
                if checkYahtzee(sortedDice):
                        yahtzeeTally.append(1)
                        lowerScore[5] = 50
                        usedSlots["yahtzee"] = True
                        print("\n...Success!\n")
                else:
                        print("no yahtzee match\n")
        if int(whereToScore) == 13:
                if usedSlots["chance"] == False:
                        calculateChance(sortedDice)
                        usedSlots["chance"] = True
                        print("\n...Success!\n")
                else:
                        print("your chance slot is full\n")
        if int(whereToScore) > 13:
                print("You entered a number larger than what was given\n")
                print("Restarting...\n")
                startRound()
                return
                
        # Calling upper bonus function
        upperBonus(upperScore)

        # Calling yahtzee bonus function
        calculateIfYahtzeeBonus()

        scoreChart()

        # return slots left to score
        slotsLeft = [slot for slot, value in usedSlots.items() if value
                     == False]
        
        print("\nSlots Left:")
        for i in slotsLeft:
              print(i + "")
        print("\nRound ended...")
        
        # Loop asking if user wants to start a new round or end the game:
        continueGame()
        return upperScore, lowerScore, str(slotsLeft)

# Start every time program is ran
print("Welcome...\n")
startGame()
