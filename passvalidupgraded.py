


while True:
    wiersz = input("Input your password to check if it is good (type end if you want to end)")
    if wiersz.lower() == 'end':
        break
    elif not any (znak.isupper() for znak in wiersz):
        print("You need atleast one uppercase letter in your password")
    
    elif not any(znak.isdigit() for znak in wiersz):
        print("You need a digit in your password")
    
    elif len(wiersz) <= 8:
        print("Your password need to contain atleast 8 characters")
    else:
        print(f"{wiersz} is a good password")

   
   