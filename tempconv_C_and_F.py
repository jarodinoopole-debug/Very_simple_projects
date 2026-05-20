operator = input("Choose what you want to calculate: C/F ")
temp = float(input("Input temperature "))
Cel = float
fah = float
if operator == 'F' or 'f':
    fah = (temp * 1.8)  + 32
    print(f"The temperature for Fahrenhait is {fah:.2f}°")
elif operator == 'C' or 'c':
    Cel = (temp - 32) * 0.5556
    print(f"The temperature for Celsius is {Cel:.2f}°")
else:
    print("Input a valid unit")