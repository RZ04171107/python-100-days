## Day 14 of 100 days python coding practice
## A higher lower game guessing which person has more followers in INS
## By Ruanqin, March 20, 2021
from art import logo
from art import vs
from game_data import data
import random
from replit import clear

#print the logo 
print(logo)
print("Welcome to the higher lower game! \n")


#function choose another person which different from the paramater
def another(dict_person_existed):
  pre_index = data.index(dict_person_existed)
  new_index = random.randint(0, len(data)-1)
  while pre_index == new_index:
    new_index = random.randint(0, len(data)-1)

  return data[new_index]
  
#two printing functions
def printA(someone_dict):
  print(f"Compare A: {someone_dict['name']}, a {someone_dict['description']}, from {someone_dict['country']}")

def printB(someone_dict):
  print(f"Against B: {someone_dict['name']}, a {someone_dict['description']}, from {someone_dict['country']}")


def compareFollowers(dictA, dictB):
  """ Return the person(as char) which has more followers """
  if dictA['follower_count'] <= dictB['follower_count']:
    return 'b'
  else:
    return 'a'


def checkGuess():
  #check the guessing result
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  moreFollower = compareFollowers(currentA, currentB)
  if guess != moreFollower:
    print(f"Sorry, that's wrong. Final score is: {previous_score}")
    return previous_score
  else:
    return previous_score + 1


currentA = {}
currentB = {}
previous_score = 0
current_score = 0

currentA = data[random.randint(0, len(data)-1)]
currentB = another(currentA)

printA(currentA)
print(vs)
printB(currentB)

current_score = checkGuess()

# stop the loop until user make a wrong guessing
while current_score > previous_score:
  previous_score = current_score
  currentA = currentB
  currentB = another(currentA)
  clear()
  print(logo)
  print(f"You are right! Current score: {current_score}")
  printA(currentA)
  print(vs)
  printB(currentB)
  current_score = checkGuess()

