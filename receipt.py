product = input("Input your product: ")
price = float(input("Input product price(in $): "))
quantity = int(input("Input quantity of products: "))
final = float
final = price * quantity

print("------------------------")
print(f"Product:       {product} ")
print(f"Price:         {price:+,.2f}$ ")
print(f"Quantity:      {quantity} ")
print("------------------------")
print(f"Final price:   {final:+,.2f}$  ")