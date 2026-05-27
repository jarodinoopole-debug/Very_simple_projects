import random
liczba = random.randint(1, 100)
guess = int 
proba = 0

def sprawdz(guess):
    if guess == liczba:
        print("You had guessed right;")
    elif guess > liczba:
        print("Too much ")
    elif guess < liczba:
        print("Too low")
    return guess

while True:
    guess = int(input("Guess a number"))
    guess = sprawdz(guess)
    proba += 1
    print(f"Number of attempts: {proba} ")
    cont = input("Do you wish to restart? Y/N/E (E for end)")
   
    if cont.lower() == 'y':
        proba = 0
        liczba = random.randint(1, 100)
    elif cont.lower() =='e':
        break
    else:
        continue 
    
    