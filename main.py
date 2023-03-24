'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# imports

import time, os, random # imports required librabries; time for refresh delay, os for screen clearing and random for question generation

# variables

[points,lives,cardnum,playagain,mode]=[0,5,0,"",""] # points = amount of cards answered correctly,lives = amount of times the player can skip an answer or answer incorrectly before the game ends, cardnum = amount of cards answered, playagain = play again placeholder and mode is the game difficulty

# cards

def startcard(): # start / title card to serve as a buffer for when the game starts
  global mode
  os.system('clear')
  print("""+----------------------------+
|                            |
| \u001b[36m  _  _  ____  ____  _  _  \u001b[0m |
| \u001b[36m | \/ || [] ||_  _|| L| | \u001b[0m |
| \u001b[36m | \/ || __ | |  | | __ | \u001b[0m |
| \u001b[36m |_||_||_||_| |__| |_||_| \u001b[0m |
| \u001b[36m      >> INFINITUM <<     \u001b[0m |
|                            |
| \u001b[35m         QUIZ GAME        \u001b[0m |
|                            |
| \u001b[34m Please Input A Game Mode \u001b[0m |
| \u001b[32m          'easy'          \u001b[0m |
| \u001b[33m         'medium'         \u001b[0m |
| \u001b[31m          'hard'          \u001b[0m |
+----------------------------+""")
  mode = input('')
  if mode == "easy": #
    print("\u001b[35mGamemode \u001b[32m'easy'\u001b[35m selected\u001b[0m")
    time.sleep(1)
  elif mode == "medium":
    print("\u001b[35mGamemode \u001b[33m'medium'\u001b[35m selected\u001b[0m")
    time.sleep(1)
  elif mode == "hard":
    print("\u001b[35mGamemode \u001b[31m'hard'\u001b[35m selected\u001b[0m")
    time.sleep(1)
  else: 
    print("\u001b[33mInvalid game mode name selected please try again\u001b[0m")
    time.sleep(1)
    startcard()      # game mode selection


def rules(): # rule card that explains what the rules are and how the game works
  os.system('clear')
  print("""+----------------------------+
| \u001b[36m          Rules:          \u001b[0m |
| \u001b[36mCards will appear one after\u001b[0m|
| \u001b[36manother, you have to answer\u001b[0m|
| \u001b[36meach card to the best of  \u001b[0m |
| \u001b[36mabilities, for every card \u001b[0m |
| \u001b[36myou answer correctly you  \u001b[0m |
| \u001b[36mearn 1 point. After""",lives,"""    \u001b[0m |
| \u001b[36mfalsely answered cards The\u001b[0m |
| \u001b[36mQuiz will end. At the end \u001b[0m |
| \u001b[36mend of the quiz your total\u001b[0m |
| \u001b[36mamount of points will be  \u001b[0m |
| \u001b[36mdisplayed for you to see. \u001b[0m |
| \u001b[34m>Press ENTER To Continue.<\u001b[0m |
+----------------------------+""")
  input('')


def card(): # draws card with custom random variables generated
  global lives,points,cardnum,mode
  cardnum += 1 # increases card number by one
  if mode == "easy": [var1,var2,operation_int] = [random.randint(0,10),random.randint(0,10),random.randint(0,3)]     #
  elif mode == "medium": [var1,var2,operation_int] = [random.randint(0,99),random.randint(0,10),random.randint(0,3)]
  elif mode == "hard": [var1,var2,operation_int] = [random.randint(0,99),random.randint(0,99),random.randint(0,3)]   # } card random question generation
  if operation_int == 0 : operation = "+"  #
  elif operation_int == 1: operation = "-"
  elif operation_int == 2: operation = "*"
  elif operation_int == 3: operation = "/" # } operation decyphering for addition, subtraction, multiplication and division
  if var1 <= 9 and var2 <= 9: operation = " "+operation+" " #
  elif var1 <= 9 or var2 <= 9: operation = " "+operation    # checks and adds correct spacing so the card graphical edges dont break
  if operation_int == 3:
    if var1 == 0: var1 = 1 #
    if var2 == 0: var2 = 1 # ZeroDivisionError prevention
  os.system('clear')
  print("""+----------------------------+
| \u001b[36mCard #""",cardnum,"""\u001b[0m
| \u001b[36mLives =""",lives,"""                \u001b[0m |
|                            |
| \u001b[35m      >> Question <<      \u001b[0m |
|                            |
| \u001b[35m        >""",var1,operation,var2,"""        \u001b[0m |
|                            |
|                            |
|                            |
|                            |
| \u001b[34m Type an acceptable answer\u001b[0m |
| \u001b[34m            Or            \u001b[0m |
| \u001b[34m Press ENTER To Skip Card \u001b[0m |
+----------------------------+""")
  try: card = float(input('')) #
  except ValueError: card = "" # } error handling
  if card == "":  #
    if operation_int == 0: print("\u001b[33mIncorrect answer or card skipped, the correct answer was:",var1 + var2,"\u001b[0m")
    elif operation_int == 1: print("\u001b[33mIncorrect answer or card skipped, the correct answer was:",var1 - var2,"\u001b[0m")
    elif operation_int == 2: print("\u001b[33mIncorrect answer or card skipped, the correct answer was:",var1 * var2,"\u001b[0m")
    elif operation_int == 3: print("\u001b[33mIncorrect answer or card skipped, the correct answer was:",round(var1 / var2,2),"\u001b[0m")
    lives -=1
    time.sleep(1) # checks if card was skipped or a non interger answer was submitted
  else:             #
    if operation_int == 0 and card == (var1 + var2) or operation_int == 1 and card == (var1 - var2) or operation_int == 2 and card == (var1 * var2) or operation_int == 3 and card == round(var1 / var2,2):
      print("\u001b[32mCorrect answer, +1 point\u001b[0m")
      points += 1
      time.sleep(2)
    else:
      if operation_int == 0: print("\u001b[31mIncorrect answer, the correct answer was:","\u001b[0m",var1 + var2,"\u001b[0m")
      elif operation_int == 1: print("\u001b[31mIncorrect answer, the correct answer was:","\u001b[0m",var1 - var2,"\u001b[0m")
      elif operation_int == 2: print("\u001b[31mIncorrect answer, the correct answer was:","\u001b[0m",var1 * var2,"\u001b[0m") 
      elif operation_int == 3: print("\u001b[31mIncorrect answer, the correct answer was:",round(var1 / var2,2),"\u001b[0m")
      lives -=1
      time.sleep(1) # checking for correct answers for the four variations of operations (add, subtract, multiply and divide) and displays if the player gets the answer wrong and what the correct answer was


def endcard(): # end card displays what the users end score was, how many cards they answered and asks them if they would like to play again
  global points, lives, cardnum, playagain
  os.system('clear')
  print("""+----------------------------+
| \u001b[33m  ____  ____  ____  ____  \u001b[0m |
| \u001b[33m |    ||    || [] ||  __| \u001b[0m |
| \u001b[33m | [] || [] || ___||__  | \u001b[0m |
| \u001b[33m |____||____||_|   |____| \u001b[0m |
| \u001b[36mIt seems you have run out \u001b[0m |
| \u001b[36mof lives, dont worry, you \u001b[0m |
| \u001b[36mmade it to card #""",cardnum,"""\u001b[0m
| \u001b[36mand earned:""",points,"""point(s)\u001b[0m
| \u001b[36mbefore your lives ran out.\u001b[0m |
|                            |
| \u001b[34mDo you want to play again \u001b[0m |
| \u001b[34mand try to beat your high \u001b[0m |
| \u001b[34mscore? (yes (y) / no (n) )\u001b[0m |
+----------------------------+""")
  playagain = input('')
  if playagain == "yes" or playagain == "y": # begins to prepare the code to play another game
    print("\u001b[35mSetting up a new game\u001b[0m")
    [points,lives,cardnum,playagain]=[0,5,0,""] # resets variables to starting values so the game can restart correctly
    time.sleep(1)
    startcard() # allows the user to change thier current gamemode
    game() # starts a new game if the player wants to start a new game
  elif playagain == "no" or playagain == "n": # displays a "thank you for playing" mesage before exiting the code
    print("\n\u001b[35mThank you for playing\u001b[0m")
    exit
  else: # retries in the case of an unexpected input
    print ("\u001b[33mUnexpected answer, please try again\u001b[0m")
    time.sleep(1)
    endcard()


def game(): # tests if the player has ran out of lives and halts the current game before displaying the end card
  global lives
  while lives >=1: card() # iterates the card code untill the player runs out of lives
  endcard() # runs the end card code
  

# game initiation order

startcard() # displays starting title card
rules() # displays rules card
game() # initiates functional game code