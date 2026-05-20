operator = input("Choose your operator: (+ - / *) ")
firstnumber = float(input("Input your first number: "))
secondnumber = float(input("Input your second number: "))
result = float
if operator == '+':
    result = firstnumber + secondnumber
    print(f"The result of addition is {result:,.2f}" )
elif operator == '-':
    result = firstnumber - secondnumber
    print(f"The result of substraction is {result:,.2f}")
elif operator == '*':
    result = firstnumber * secondnumber
    print(f"The result of substraction is {result:,.2f}")
elif operator == '/':
    result = firstnumber / secondnumber
    print(f"The result of substraction is {result:,.2f}")

else:
    print("Error invalid operator ")