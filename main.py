'''
  Name: 
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# imports

import os, random


# cards

def startcard():
  os.system('clear')
  print("+----------------------------+")
  print("|                            |")
  print("|   _  _  ____  ____  _  _   |")
  print("|  | \/ || [] ||_  _|| L| |  |")
  print("|  | \/ || __ | |  | | __ |  |")
  print("|  |_||_||_||_| |__| |_||_|  |")
  print("|       >> INFINITUM <<      |")
  print("|                            |")
  print("|          QUIZ GAME         |")
  print("|                            |")
  print("|                            |")
  print("|         Press ENTER        |")
  print("|          To Begin          |")
  print("|                            |")
  print("+----------------------------+")
  input('')


def rules():
  os.system('clear')
  print("+----------------------------+")
  print("|           Rules:           |")
  print("| Cards will appear one after|")
  print("| another, you have to answer|")
  print("| each card to the best of   |")
  print("| abilities, for every card  |")
  print("| you answer correctly you   |")
  print("| earn 1 point. After",lives,"     |")
  print("| falsely answered cards The |")
  print("| Quiz will end. At the end  |")
  print("| end of the quiz your total |")
  print("| amount of points will be   |")
  print("| displayed for you to see.  |")
  print("| >Press ENTER To Continue.< |")
  print("+----------------------------+")
  input('')


def card():
  global lives
  var1 = random.randint(10,99)
  operation_int = random.randint(0,3)
  if operation_int == 0 : operation = "+"
  elif operation_int == 1 : operation = "-"
  elif operation_int == 2 : operation = "*"
  elif operation_int == 3 : operation = "/"
  var2 = random.randint(10,99)
  os.system('clear')
  print("+----------------------------+")
  print("| Card #",cardnum)
  print("| Lives =",lives,"                 |")
  print("|                            |")
  print("|       >> Question <<       |")
  print("|                            |")
  print("|         >",var1,operation,var2,"         |")
  print("|                            |")
  print("|                            |")
  print("|                            |")
  print("|                            |")
  print("|  Type an acceptable answer |")
  print("|             Or             |")
  print("|  Press ENTER To Skip Card  |")
  print("+----------------------------+")
  card = input('')
  if card == "":
    lives -=1
    

    
def endcard():
  print("end")

# variables

points = 0
lives = 5
cards = 0
cardnum = 1

# code testing

startcard()
rules()
while lives >=1: card()

endcard()