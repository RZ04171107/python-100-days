from replit import clear
from art import logo

auction = {}

def add_new_bid(name, money):
  auction[name] = money

def ask_user_input():
  name = input("What is your name? ")
  bid = int(input("What is your bit? $"))
  add_new_bid(name, bid)

def get_highest_bid():
  highest = 0
  winner = ""
  for bidder in auction:
    if auction[bidder] >= highest:
      highest = auction[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest}")

print(logo)
print("Welcome to the blind auction!")
continue_auction = True

while continue_auction:
  ask_user_input()
  continue_str = input("Are there any other bidders? Type 'yes' or 'no'.")
  if continue_str=='yes':
    continue_auction = True
    clear()   
  elif continue_str == 'no':
    continue_auction = False
    clear()
    get_highest_bid() 
  else:
    continue_auction = False
    print("Oops,input error!")


