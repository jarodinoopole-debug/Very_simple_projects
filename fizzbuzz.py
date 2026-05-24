limit = int(input("Enter an value: "))
for number in range(1, limit + 1):
    if number % 5 == 0 and number % 3 == 0:
        print("Fizzbuzz")        
    elif number % 5 == 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    