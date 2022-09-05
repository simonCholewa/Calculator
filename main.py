from logo import logo
from replit import clear

# -------------------------- Add --------------------------
def add(a, b):
  return a + b

# -------------------------- Substract --------------------------
def substract(a, b):
  return a - b

# -------------------------- Multiply --------------------------
def multiply(a, b):
  return a * b

# -------------------------- Divide --------------------------
def divide(a, b):
  return a / b

# -------------------------- Modulo --------------------------
def modulo(a, b):
  return a % b


# Operations dictionary
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}


def calculator():
  print(logo)

  num1 = float(input("Enter first number: "))
  print("Avilable operations: ")
  for key in operations:
    print(key)
  
  stop_program = False

  while not stop_program:
    chosen_operation = input("Pick and operation: ")
    num2 = float(input("Enter second number: "))
    calc_function = operations[chosen_operation]
    result = calc_function(num1, num2)
    print(f"{num1} {chosen_operation} {num2} = {result}")

    choice = input("To contiune type y. To stop type n: ")

    if choice == "y":
      num1 = result
    else:
      stop_program = True
      clear()
      calculator()

calculator()