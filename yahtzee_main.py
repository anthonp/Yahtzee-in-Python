import random
from random import randint

# User section:--------------------------------------------

# Load old data:---------------

# Use loadOldSave() to load previous save data:
def loadOldSave():
    with open("yahtzee_save.txt", "r") as input:
        return yahtzeeTally, slotsLeft, upperScore, lowerScore, usedSlots

# End a current game:---------------

# Total total game points:
# To total the game, at the end of all rounds, type "endGame()"
# "endGame()" prompts the user to save the game if they wish
def endGame(yahtzeeTally, slotsLeft, upperScore, lowerScore, usedSlots):
        with open("yahtzee_save.txt", "w") as input:
            print("The total score for you is: ")
            print(totalling())
            print("Upper Score: " + ''.join(str(upperScore)))
            print("Lower Score: " + ''.join(str(lowerScore)))

# Start a new game:----------------

# Run game using "startGame()"; starts a completely fresh game.
# The dictionary returns items as you play the game.
def startRound():
        game(upperScore, lowerScore, sortedDice, usedSlots)
        
# Initialization Section:----------------------------------

# Yahtzee tally
yahtzeeTally = []

# Initialized dice list
sortedDice = [0, 0, 0, 0, 0]

# List of unused scores
slotsLeft = []

# Upper and Lower scores; last upper position holds 35 pt bonus
upperScore = [0, 0, 0, 0, 0, 0, 0] # index 0-5, but values 1-6;
lowerScore = [0, 0, 0, 0, 0, 0, 0, 0] # indices for lower scores

# Used/unused slots:
usedSlots = {"1's":False, "2's":False, "3's":False, "4's":False, "5's":False,
             "6's":False, "bonus yahtzee":False, "3 of a kind":False, 
             "4 of a kind":False, "full house":False, "small straight":False, 
             "large straight":False, "yahtzee":False, "chance":False}

#def initSavedGame():

# Core Components:-----------------------------------------

# Rolling of the dice:
def rollingAction():
    sortedDice.clear()
    for d in range(5):
        sortedDice.append(randint(1,6))
    return sortedDice.sort()

# Change of the dice by user:
def roll():
    diceOne()
    diceTwo()
    diceThree()
    diceFour()
    diceFive()
    return sortedDice.sort()

# Used for new scoring system:
def getDieInput(param):
    posInput = input(param)
    return posInput

# Handles sanitization asking user if they want to save:
def saveSanitization(stringInput, number, dice):
    if (str(stringInput)).lower() == 'y':
        print("Keeping #" + str(number) + "...\n")
        return sortedDice.sort()
    if (str(stringInput)).lower() == 'n':
        sortedDice[int(number) - 1] = (randint(1,6))
        print("Updated\n")
        return sortedDice.sort()
    if (str(stringInput)).lower() != "n" or "y":
        print("\ninvalid entry...\n")
        dice()

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
        if(all(i in myRoll for i in patternOne)):
            return True
        if(all(i in myRoll for i in patternTwo)):
            return True
        if(all(i in myRoll for i in patternThree)):
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

# Check and add a yahtzee to tally:
def checkYahtzee(sortedDice):
        if sortedDice[0] == sortedDice[4]:
                return True
        else:
                return False

# Calculate chance
def calculateChance(sortedDice):
        lowerScore[6] = sum(sortedDice)

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
        # Condensed for readability in game:
        print("Scoring Key:\n------------------\nEnter 1 for 1's")
        print("Enter 2 for 2's\nEnter 3 for 3's\nEnter 4 for 4's")
        print("Enter 5 for 5's\nEnter 6 for 6's\n------------------")
        print("Enter 7 for 3 of a kind\nEnter 8 for 4 of a kind")
        print("Enter 9 for full house\nEnter 10 for small straight")
        print("Enter 11 for large straight\nEnter 12 for yahtzee")
        print("Enter 13 for chance\n------------------\nSlots Left: ")
        slotsLeft = [slot for slot, value in usedSlots.items() if value
                     == False]
        for i in slotsLeft:
              print(i + "")
        print("\nWhichever is selected will be checked\n------------------")

# Dice calls:
def diceOne():
    print("Would you like to keep dice #1? ")
    pos1 = getDieInput("Enter 'y' or 'n': ")
    # sanitizeUserInput() serves to sanitize the
    # input from users that might be malformed.
    sanitizeUserInput(pos1, 1, diceOne)
def diceTwo():
    print("Would you like to keep dice #2? ")
    pos2 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos2, 2, diceTwo)
def diceThree():
    print("Would you like to keep dice #3? ")
    pos3 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos3, 3, diceThree)
def diceFour():
    print("Would you like to keep dice #4? ")
    pos4 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos4, 4, diceFour)
def diceFive():
    print("Would you like to keep dice #5? ")
    pos5 = getDieInput("Enter 'y' or 'n': ")
    sanitizeUserInput(pos5, 5, diceFive)
    print("Your dice so far: " + str(sortedDice[0]) + ", "
          + str(sortedDice[1]) + ", " + str(sortedDice[2]) + ", "
          + str(sortedDice[3]) + ", " + str(sortedDice[4]) + "\n")
    return sortedDice.sort()
    
# Sanitize User Input for dice rolls:
def sanitizeUserInput(stringInput, number, dice):
    if (str(stringInput)).lower() == 'y':
        print("Keeping #" + str(number) + "...\n")
        return sortedDice.sort()
    if (str(stringInput)).lower() == 'n':
        sortedDice[int(number) - 1] = (randint(1,6))
        print("Updated\n")
        return sortedDice.sort()
    if (str(stringInput)).lower() != "n" or "y":
        print("\ninvalid entry...\n")
        dice()

# Core game function:
def game(upperScore, lowerScore, sortedDice, usedSlots):
        print("Copyright Anthony Picciano, 2021")
        print("\nROLL ONE:")
        print("Rolling...\nDumping cup...\n")
        rollingAction() # First roll.
        print("Current Roll: " + str(sortedDice[0]) + ", "
          + str(sortedDice[1]) + ", " +
          str(sortedDice[2]) + ", " +
          str(sortedDice[3]) + ", "
          + str(sortedDice[4]))
        # Asking if user wants a second roll:
        print("Would you like a SECOND ROLL? ")
        # Roll two determination function
        rollTwo = getDieInput("Enter 'y' or 'n': ")
        if (str(rollTwo)).lower() == "y":
                print("\nROLL TWO:")
                roll() # Second roll.
        elif (str(rollTwo)).lower() == "n":
                print("")
                print("Current dice: " + str(sortedDice[0]) + ", "
                      + str(sortedDice[1]) + ", " + str(sortedDice[2]) + ", "
                      + str(sortedDice[3]) + ", " + str(sortedDice[4]) + "\n")
        else:
                print("\n\nError with your input, exiting\n")
                return
        # Asking if user wants a third roll:
        print("Would you like your THIRD ROLL? ")
        # Roll three determination function
        rollThree = getDieInput("Enter 'y' or 'n': ")
        if (str(rollThree)).lower() == "y":
                print("\nROLL THREE:")
                roll() # Third roll.
        elif (str(rollThree)).lower() == "n":
                print("")
                print("Current dice: " + str(sortedDice[0]) + ", "
                      + str(sortedDice[1]) + ", " + str(sortedDice[2]) + ", "
                      + str(sortedDice[3]) + ", " + str(sortedDice[4]) + "\n")
        else:
                print("\n\nError with your input, exiting\n")
                return
        # Calling the score sheet:
        scoringKey()
        print("How do you want to score " + str(sortedDice[0]) + ", "
              + str(sortedDice[1]) + ", " +
              str(sortedDice[2]) + ", " + str(sortedDice[3])
              + ", " + str(sortedDice[4]) + "?")
        whereToScore = getDieInput("Enter a number: ")

        if whereToScore.isalpha():
                print("\nYou entered a string, not a number\n")
                print("Shutting down...\n")
                return
        if int(whereToScore) == 1:
                if usedSlots["1's"] == False and 1 in sortedDice:
                        upperScore[0] = sortedDice.count(1)
                        usedSlots["1's"] = True
                        print("\n...Success!\n")
                else:
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
                        print("")
                        print("...Success!")
                        print("")
                else:
                        print("6's are full/dice don't match\n")
        if int(whereToScore) == 7:
                if checkThreeKind(sortedDice) and usedSlots["3 of a kind"] == False:
                        lowerScore[0] = sum(sortedDice)
                        usedSlots["3 of a kind"] = True
                        print("\n...Success!\n")
                else:
                        print("3 of a kind full/no match\n")
        if int(whereToScore) == 8:
                if checkFourKind(sortedDice) and usedSlots["4 of a kind"] == False:
                        lowerScore[1] = sum(sortedDice)
                        usedSlots["4 of a kind"] = True
                        print("\n...Success!\n")
                else:
                        print("4 of a kind full/no match\n")
        if int(whereToScore) == 9:
                if checkFullHouse(sortedDice) and usedSlots["full house"] == False:
                        lowerScore[2] = 25
                        usedSlots["full house"] = True
                        print("\n...Success!\n")
                else:
                        print("full house full/no match\n")
        if int(whereToScore) == 10:
                if checkSmallStraight(sortedDice) and usedSlots["small straight"] == False:
                        lowerScore[3] = 30
                        usedSlots["small straight"] = True
                        print("\n...Success!\n")
                else:
                        print("small straight full/no match\n")
        if int(whereToScore) == 11:
                if checkLargeStraight(sortedDice) and usedSlots["large straight"] == False:
                        lowerScore[4] = 40
                        usedSlots["large straight"] = True
                        print("\n...Success!\n")
                else:
                        print("large straight full/no match\n")
        if int(whereToScore) == 12:
                if checkYahtzee(sortedDice) and usedSlots["yahtzee"] == False:
                        yahtzeeTally.append(1)
                        lowerScore[5] = 50
                        usedSlots["yahtzee"] = True
                        print("\n...Success!\n")
                else:
                        print("yahtzee full/no match\n")
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
                return
                
        # Calling upper bonus function
        upperBonus(upperScore)
        print("Upper bonus calculated...\nSum of upper so far:")
        print(str(sum(upperScore)) + " points\n")

        # Calling yahtzee bonus function
        calculateIfYahtzeeBonus()
        print("Yahtzee bonus calculated...")
        print("Your Yahtzees: " + str(sum(yahtzeeTally)) + "\n")

        # return slots left to score
        slotsLeft = [slot for slot, value in usedSlots.items() if value
                     == False]
        
        print("Upper Score: " + ''.join(str(upperScore)))
        print("Lower Score: " + ''.join(str(lowerScore)) + "\nSlots Left:")
        for i in slotsLeft:
              print(i + "")
        print("\n\nRound ended...\n\nType 'startRound()' to go again...")
        return upperScore, lowerScore, str(slotsLeft)

# Start every time program is ran
print("Starting Round...\n")
startRound()
