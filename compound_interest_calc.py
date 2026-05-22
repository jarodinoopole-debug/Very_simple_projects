import math
currency = input("Input your currency: ")
principal = input("Enter your principal income: ")

while isinstance(principal, str) :
    print("Enter again given value: ")
    principal = input("")
    try:
        principal = float(principal)
    except ValueError:
        print("Error enter a valid number")

interest_rate = input("Input your interest rate: ")

while isinstance(interest_rate, str) :
    print("Enter again given value: ")
    interest_rate = input("")
    try:
        interest_rate = float(interest_rate)
    except ValueError:
        print("Error enter a valid number")

years = input("Input years: ")        

while isinstance(years, str) :
    print("Enter again given value: ")
    years = input("")
    try:
        years = float(years)
    except ValueError:
        print("Error enter a valid number")

frequency = input("Input frequency: ")        

while isinstance(frequency, str):
    print("Enter again given value: ")
    frequency = input("")
    try:
        frequency = int(frequency)
    except ValueError:
        print("Error enter a valid number")
while frequency % 2 != 0:
    frequency = int(input("Enter an even number "))

result = float
interest_rate = interest_rate / 100
result = principal * pow(1 + interest_rate / frequency, frequency * years )
print(f"After {years} years balance will be {result:.2f}{currency}")

      
    