nameuser = input("Input your username.")
if len(nameuser) > 12 or len(nameuser) < 3:
    print("Username min letters can't be lower than 3 and can't be more than 12. ")
elif nameuser.find(" ") != -1:
    print("Username can't contain any spaces. ")
elif not nameuser.isalpha():
    print("Username can contain only letters. ")
elif nameuser[0] != nameuser.capitalize()[0]:
    print("Username needs to be started with an upper case letter. ")
else:
    print(f"{nameuser} is a good username. ")