#Program by Evan Prael
#Date: November 1, 2024
#Description: 
#   This program asks three questions and gives a score at the end
#   The user gets a random consequence for wrong answers.

#   It stores the questions, answers and consequences in collections.
#   It picks 3 random questions from a set of 8, and a random consequence 
#   if the answer is wrong.   
#
#   The user gets an added consequence if they get them all wrong.
#
#   Program written with help from Github CoPilot
#   Tested in VS Code for Windows

# need this to clear the screen
from os import system, name

# need this to use random function
import random

import time

# codes for printing colored replies (red - incorrect, green - correct, yellow - consequence
# found here https://stackoverflow.com/questions/58030468/how-to-have-colors-in-terminal-with-python-in-vscode/72970140#72970140
color_red = "\033[31m"
color_green = "\033[32m"
color_yellow= "\033[33m"
color_end = "\033[0m"

# number of questions to ask.  
# must be less than the number of questions in the following list
numOfQuestions = 3

questionAnswers = [ ["What is the capital of Canada? ", "Ottawa"],
                    ["Is Pluto a planet? y/n? ", "n"],
                    ["Which planet is bigger - Jupiter or Saturn? ", "Jupiter"],
                    ["In what year was the 'Battle of 1812'? ", "1812"],
                    ["How many swords are there in Minecraft - 5, 6, 8, 99? ", "6"],
                    ["What is -1 squared? ", "1"],
                    ["How many seconds are there in a day? ", "86400"],
                    ["How many minutes does it take for the space station to orbit the earth? ", "92"]]

consequences = ["You've lost your wallet!", 
                "You've just caused the sun to go dark!", 
                "The sky just fell on your head!", 
                "The moon just crashed into Africa!",
                "Your dog just knocked over the flowers. They're ruined!",
                "The cat didn't make it to the litterbox and it really smells.",
                "You just got teleported to a Minecraft dungeon!"]


# from github copilot
# function to clear the screen using escape codes
def clear_screen():
  print ("\033[2J\033[0;0f", end="")


# function with 3 parameters: question, answer, and consequence for incorrect answer
# returns 1 if the answer is correct, 0 if incorrect
def question_answer(question, correctAnswer, consequence):
    answer = ""
    tries = 0
    
    # this loop will keep asking the same question up to 3 times until an answer is entered
    while answer == "" and tries < 3:
        tries += 1     
        answer=input(question)
        
        time.sleep(1)
        
        if answer == "":
            print ("")
            print (color_red + "You did not give an answer, please try again." + color_end)
            print ("")
            time.sleep(1)
            

    if answer == correctAnswer:
        print ("")
        print (color_green + "Correct!" + color_end)
        print ("")
        time.sleep(1)
        return 1
    else :
        print ("")
        print (color_red + "Incorrect. The correct answer is " + correctAnswer+color_end)
        print ("")
        time.sleep(1)
        print(color_yellow + consequence + color_end)
        print ("")
        time.sleep(2)
        
    print ("")
    return 0


# ----------------------------------------------------

# this is the main program.
# It calls the question_answer function three times and each time adds the return code to the main score (0 or 1).

# clear the screen
clear_screen()

# multi-line print statement
print("""Welcome to the game 'Answer-or-Else'
------------------------------------

You will be asked three questions. Each correct answer is worth one point.
Incorrect answers will result in a *terrible* consequence!!
Remember, spelling/capitalization is important!

Good luck! 
""")

input("Press Enter to continue...")

print ("")

play_again="y"

while play_again=="y":

    score = 0

    # clear the screen
    clear_screen()

    # get a random starting point from the list of questions
    startIndex = random.randrange(0,len(questionAnswers)-numOfQuestions)
 
    
    # ask the three questions
    for i in range(1,(numOfQuestions+1)):
        
        questionIndex = startIndex + i
        
        
        # call the question_answer function and add the return code to the score
        score += question_answer(str(i) + ". " + questionAnswers[questionIndex][0], 
                                 questionAnswers[questionIndex][1], 
                                 random.choice(consequences))

    print ("Your score is", score, "out of ", str(numOfQuestions), "!")

    print ("")

    if score == numOfQuestions:
        print ("You're a genius!!")
    elif score == 0:    
        print(color_yellow + random.choice(consequences) + color_end)
        time.sleep(1)
    else:
        print ("Better luck next time!") 
        
    print ("")

    play_again=input("Play again (y/n)? ")
    
    print ("")

print("Thanks for playing!")

print("")
