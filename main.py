'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# imports

import time, os, random

# variables

points = 0
lives = 5
cards = 0
cardnum = 0
playagain = "n"


# cards

def startcard():
  os.system('clear')
  print("+----------------------------+")
  print("|                            |")
  print("| \u001b[36m  _  _  ____  ____  _  _  \u001b[0m |")
  print("| \u001b[36m | \/ || [] ||_  _|| L| | \u001b[0m |")
  print("| \u001b[36m | \/ || __ | |  | | __ | \u001b[0m |")
  print("| \u001b[36m |_||_||_||_| |__| |_||_| \u001b[0m |")
  print("| \u001b[36m      >> INFINITUM <<     \u001b[0m |")
  print("|                            |")
  print("| \u001b[35m         QUIZ GAME        \u001b[0m |")
  print("|                            |")
  print("|                            |")
  print("| \u001b[34m        Press ENTER       \u001b[0m |")
  print("| \u001b[34m         To Begin         \u001b[0m |")
  print("|                            |")
  print("+----------------------------+")
  input('')


def rules():
  os.system('clear')
  print("+----------------------------+")
  print("| \u001b[36m          Rules:          \u001b[0m |")
  print("| \u001b[36mCards will appear one after\u001b[0m|")
  print("| \u001b[36manother, you have to answer\u001b[0m|")
  print("| \u001b[36meach card to the best of  \u001b[0m |")
  print("| \u001b[36mabilities, for every card \u001b[0m |")
  print("| \u001b[36myou answer correctly you  \u001b[0m |")
  print("| \u001b[36mearn 1 point. After",lives,"    \u001b[0m |")
  print("| \u001b[36mfalsely answered cards The\u001b[0m |")
  print("| \u001b[36mQuiz will end. At the end \u001b[0m |")
  print("| \u001b[36mend of the quiz your total\u001b[0m |")
  print("| \u001b[36mamount of points will be  \u001b[0m |")
  print("| \u001b[36mdisplayed for you to see. \u001b[0m |")
  print("| \u001b[34m>Press ENTER To Continue.<\u001b[0m |")
  print("+----------------------------+")
  input('')


def card():
  global lives,points,cardnum
  cardnum += 1
  var1 = random.randint(10,99)
  operation_int = random.randint(0,3)
  if operation_int == 0 : operation = "+"
  elif operation_int == 1 : operation = "-"
  elif operation_int == 2 : operation = "*"
  elif operation_int == 3 : operation = "/"
  var2 = random.randint(10,99)
  os.system('clear')
  print("+----------------------------+")
  print("| \u001b[36mCard #",cardnum,"\u001b[0m")
  print("| \u001b[36mLives =",lives,"                \u001b[0m |")
  print("|                            |")
  print("| \u001b[35m      >> Question <<      \u001b[0m |")
  print("|                            |")
  print("| \u001b[35m        >",var1,operation,var2,"        \u001b[0m |")
  print("|                            |")
  print("|                            |")
  print("|                            |")
  print("|                            |")
  print("| \u001b[34m Type an acceptable answer\u001b[0m |")
  print("| \u001b[34m            Or            \u001b[0m |")
  print("| \u001b[34m Press ENTER To Skip Card \u001b[0m |")
  print("+----------------------------+")
  try:
    card = float(input(''))
  except ValueError:
    card = ""
  
  if card == "":
    print("Incorrect answer or card skipped")
    lives -=1
    time.sleep(1)
    
  elif operation_int == 0:
    if card == (var1 + var2):
      print("\u001b[32mCorrect answer, +1 point\u001b[0m")
      points += 1
      time.sleep(2)
    else:
      print("\u001b[31mIncorrect answer, the correct answer was:",var1 + var2,"\u001b[0m")
      lives -=1
      time.sleep(1)
    
  elif operation_int == 1:
    if card == (var1 - var2):
      print("\u001b[32mCorrect answer, +1 point\u001b[0m")
      points += 1
      time.sleep(2)
    else:
      print("\u001b[31mIncorrect answer, the correct answer was:","\u001b[0m",var1 - var2,"\u001b[0m")
      lives -=1
      time.sleep(1)
    
  elif operation_int == 2:
    if card == (var1 * var2):
      print("\u001b[32mCorrect answer, +1 point\u001b[0m")
      points += 1
      time.sleep(2)
    else:
      print("\u001b[31mIncorrect answer, the correct answer was:","\u001b[0m",var1 * var2,"\u001b[0m")
      lives -=1
      time.sleep(1)
    
  elif operation_int == 3:
    if card == round(var1 / var2,2):
      print("\u001b[32mCorrect answer, +1 point\u001b[0m")
      points += 1
      time.sleep(2)
    else:
      print("\u001b[31mIncorrect answer, the correct answer was:",round(var1 / var2,2),"\u001b[0m")
      lives -=1
      time.sleep(1)




def endcard():
  global points, cards, lives, cardnum, playagain
  os.system('clear')
  print("+----------------------------+")
  print("| \u001b[36m  ____  ____  ____  ____  \u001b[0m |")
  print("| \u001b[36m |    ||    || [] ||  __| \u001b[0m |")
  print("| \u001b[36m | [] || [] || ___||__  | \u001b[0m |")
  print("| \u001b[36m |____||____||_|   |____| \u001b[0m |")
  print("| \u001b[36mIt seems you have run out \u001b[0m |")
  print("| \u001b[36mof lives, dont worry, you \u001b[0m |")
  print("| \u001b[36mmade it to card #",cardnum,"\u001b[0m")
  print("| \u001b[36mand earned:",points,"point(s)\u001b[0m")
  print("| \u001b[36mbefore your lives ran out.\u001b[0m |")
  print("|                            |")
  print("| \u001b[34mDo you want to play again \u001b[0m |")
  print("| \u001b[34mand try to beat your high \u001b[0m |")
  print("| \u001b[34mscore? (yes (y) / no (n) )\u001b[0m |")
  print("+----------------------------+")
  playagain = input('')
  if playagain == "yes" or playagain == "y":
    print("\u001b[35mSetting up a new game\u001b[0m")
    points = 0
    lives = 5
    cards = 0
    cardnum = 0
    time.sleep(1)
    game()
  elif playagain == "no" or playagain == "n":
    print("\u001b[35mThank you for playing\u001b[0m")
    exit
  else:
    print ("\u001b[33mUnexpected answer, please try again\u001b[0m")
    time.sleep(1)
    endcard()


def game():
  global lives
  while lives >=1: card()
  endcard()


# code testing

startcard()
rules()
game()