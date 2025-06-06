# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
# This calculator will provide an error if the values of a, b, or c do not properly satisfy Heron's formula.
import math
a = float(input("What is side A?: "))
b = float(input("What is side B?: "))
c = float(input("What is side C?: "))
units = str(input("What is the unit of measurement?: "))
s = (a + b + c) / 2
area = math.sqrt(s*(s - a)*(s - b)*(s -c))
print(f"The area of this triangle is {area} {units}!")
