# Day 11 of python coding practice
# By Ruanqin, March 18th, 2021
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############### Our Blackjack House Rules #####################

from art import logo
from replit import clear
import random

def startGame():
  clear()
  print(logo)
  overflow = False
  bothPass = False
  global user_pass
  global comp_pass
  #at the beginning, the user should get 2 cards
  user_list.append(getCard())
  user_list.append(getCard())

  #computer also get 2 cards, but only the first card can be seen by the user
  comp_list.append(getCard())
  comp_list.append(getCard())

  showCurrentScore()
  if getUserScore()>=21 or getComputerScore()>=21:
      overflow = True

  while overflow==False and bothPass==False:
    
    #ask for user's input to decide if get another card or not
    ifCont = input("Type 'y' to get another card, type 'n' to pass: ")
    turnOfUser(ifCont)   
    
    if getUserScore()>=21 or getComputerScore()>=21:
      overflow = True
    bothPass = user_pass and comp_pass

  print(f"user:{getUserScore()}  computer:{getComputerScore()}")
  examTheResult()
  #if the user wants to play again, call startGame() recursively
  if input("Want to play Blackjack again? Type 'y' or 'n': ")=='y':
    initialize_variables()
    startGame()
  else:
    print("Au revoir...")

def showCurrentScore(): 
  #compute and print out the current score
  print(f"Your cards: {user_list}, current score: {getUserScore()}")
  print(f"Computer's first card: {comp_list[0]}")
  #print(f"For debug: Computer's cards: {comp_list}, total score: {getComputerScore()}")

#exam the total score for both sides, see if the game is ended
def examTheResult():
  
  user_total_score = getUserScore()
  comp_total_score = getComputerScore()
  
  if user_total_score > 21 and comp_total_score >21:
    print("Draw!")
  elif user_total_score > 21:
    print("You lose. The dealer wins.")
  elif comp_total_score > 21:
    print("You win!")
  else:
    #none of both sides cross 21 point, compare their total scores
    if user_total_score < comp_total_score:
      print("You lose. The dealer wins.")
    elif user_total_score > comp_total_score:
      print("You win!")
    else:
      print("Draw!")


def getComputerScore():
  return countScore(comp_list)

def getUserScore():
  return countScore(user_list)

#each round starts from the user,
#and the user can decide either add card or not
#the return value is if the user already stopped adding any card
def turnOfUser(command_char):
  #add card
  if command_char == 'y':
    user_list.append(getCard())
  else:
    global user_pass
    user_pass = True
  #print(f"@@ user pass:{user_pass}")
  turnOfComputer()

#each round, the computer has 2 different dicision
#In my game, the computer does not want to take any risk
#So when score >= 17, the computer won't add any other card
#the return value of this function is if the computer already stopped adding any card
def turnOfComputer():
 
  #add card
  if getComputerScore() < 17:
    comp_list.append(getCard())
  else:
    global comp_pass
    comp_pass = True
  #print(f"@@ computer pass:{comp_pass}")
  showCurrentScore()
 

def countScore(cardList):
  totalScore = sum(cardList)
  #need to know if Ace is in the card list
  if 11 in cardList and totalScore > 21:   
    #when Ace exists, first count Ace as 11
    #if the total score is over 21, then try to count Ace as 1
    cardList.remove(11)
    cardList.append(1)
    countScore(cardList)

  return totalScore

def getCard():
  #giving the cards pool
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

#initiate some global variables
def initialize_variables():
  global user_list
  global comp_list
  global user_total_score 
  global comp_total_score
  global user_pass
  global comp_pass
  user_list = []
  comp_list = []
  user_total_score = 0
  comp_total_score = 0
  user_pass = False
  comp_pass = False

initialize_variables()

#at the first beginning, ask the user 
ifStart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if ifStart == 'y':
  startGame()
else:
  print("Au revoir...")
