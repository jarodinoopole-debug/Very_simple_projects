stop = 'stop'
cart = []
price = []
currency = input("Input currency: ")
while stop.lower() != 'done':
    item = input("Input name of item: ")
    cart.append(item)
    price1 = float(input("Enter an item price "))
    price.append(price1)
    stop = input("If you want to see the result type 'Done' if you want to add more enter any key: ")
else:
    print(f"The receipt is:")
    print("--------------")
for p, c in zip(cart, price):
    
    print(p, c, currency)
print("--------------")