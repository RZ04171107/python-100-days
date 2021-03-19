## A simple number guessing game
## Day 12 of python 100 days coding practice
## By Ruanqin, March 19th,2021
import random
from art import logo
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
theNumber = random.randint(1,100)
timeLeft = -1
EASY_TURNS = 10
HARD_TURNS = 5
#a function to ask the user to initiate timeLeft
def setDifficulty():
  if input("Choose a difficulty. Type 'easy' or 'hard': ")=='easy':
    return EASY_TURNS
  else:
    return HARD_TURNS

guessRight = False
timeLeft = setDifficulty()
while guessRight==False and timeLeft > 0:
  #at the start of each round, 
  #tell user timeLeft and ask the user for input
  print(f"You have {timeLeft} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

  #if the guessing is correct,end the game
  if guess == theNumber:
    print(f"Congratulation! {guess} is the number that I thought.")
    guessRight = True
  else:
    if guess < theNumber:
      print("Too low.")
    else:
      print("Too high.")
    print("Guess again.")
    timeLeft -= 1

if guessRight == False and timeLeft == 0:
  print("You have run out of guesses. You lose.")

