from art import logo
from replit import clear
# A simple calculator created by Ruanqin
# Only has add, substract, multiply and divide operation.
# Day 10 of python coding practice, March 18th,2021 

#add
def add(num1,num2):
  return num1+num2

#substract
def substract(n1,n2):
  return n1-n2

#multiply
def multiply(n1,n2):
  return n1*n2

#divide
def divide(n1,n2):
  return n1/n2

def start_new_calculation():
  
  new_culculate = True
  while new_culculate:
    
    num1 = float(input("Please enter the first number. "))

    #first print the keys of the dictionary
    for key in operation_dic:
      print(key)

    chosen_key = input("Please pick an operation from above. ")
    num2 = float(input("Please enter the second number. "))

    res = round(operation_dic[chosen_key](num1,num2),2)
    print(f"{num1} {chosen_key} {num2}  =  {res}")

    #ask the user if contunue 
    ifContinue = input("Do you want to use your answer for further cuculation (type:'y'), start a new culculation (tpye:'n'), or ending the calculation(type: 'e') ?")

    if ifContinue == 'y':
      new_culculate = False
      contunue_calculate(res)
    elif ifContinue == 'n':
      new_culculate = True
      clear()
    else:
      print("End of calculation. Thanks for using, goodbye! ")
      new_culculate = False

def contunue_calculate(privious_res):
  clear()
  print(f"Your previous answer is {privious_res}")
  for key in operation_dic:
      print(key)
  chosen_key = input("Please pick an operation from above. ")
  num3 = float(input("Please enter another number. "))
  
  res = round(operation_dic[chosen_key](privious_res,num3),2)
  print(f"{privious_res} {chosen_key} {num3}  =  {res}")

  #ask the user if contunue 
  ifContinue = input("Do you want to use your answer for further cuculation (type:'y'), start a new culculation (tpye:'n'), or ending the calculation(type: 'e') ?")

  if ifContinue == 'y':
    #call the continue_culculate() recursively
    contunue_calculate(res)
  elif ifContinue == 'n':
    clear()
    start_new_calculation()
  else:
    print("End of calculation. Thanks for using, goodbye! ")

#link the simbles and the functions with a dictionary
#values are the functions' name
operation_dic = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}
print(logo)
print("Welcome to the mini cuculator!")
start_new_calculation()


