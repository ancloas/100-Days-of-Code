from art import logo

# Add
def add(n1, n2):
  return n1+n2


# Substract
def subs(n1, n2):
  return n1-n2


# multiply
def multipy(n1, n2):
  return n1*n2

# divide
def divide(n1, n2):
  return n1 / n2

operations={
  '/': divide, 
  '*': multipy,
  '-': subs,
  '+': add,
}

#calc function
def calculator(new_num, num1=0):
  print(logo)
  if new_num:
    num1=float(input("What's the first number?: "))
    for symbol in operations:
      print(f'{symbol}')
    
  operation=input("""what's the desired operation? """)
  num2=float(input("What's the next number?: "))
  
  result =calculate(num1, operation, num2)
  print(f'{num1} {operation} {num2} = {result}')
  
  to_continue=input(f"type y' to continue calculating with {result}, or type 'n to start new calculation, or type 'exit' to exit: ")
  if to_continue.lower()=='y':
    calculator(False, result)
  elif to_continue.lower()=='n':
    calculator(new_num=True)
  return result


def calculate(num1, operation, num2):
  calc_function=operations[operation]
  result=calc_function(num1, num2)
  return result


calculator(new_num=True)



