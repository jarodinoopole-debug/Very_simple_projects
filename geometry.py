import math


print("In this program u will calculate circle circuit, area of a circle and hypotenuse(in cm). ")
radius = float(input("Input a radius of a circle: "))
side_a = float(input("Input side a of a triangle: "))
side_b = float(input("Input side b of a triangle: "))

circuit = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print("-----------------------------------------")
print(f"The circuit of a circle is {circuit:.2f}cm. ")
print("-----------------------------------------")
print(f"The area of a circle is {area:.2f}cm^2")
print("-----------------------------------------")
print(f"The hypotenuse is {hypotenuse:.2f}cm")
print("-----------------------------------------")