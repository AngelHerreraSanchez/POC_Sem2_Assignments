
try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number"))
except ValueError:
    print("An interger wasn't given")

try:
    print(number1/number2)
except ZeroDivisionError:
    print("Division by zero is not possible") 

