# 4. Create a program that prompts the user for their birth year and displays a message that says "You are ___ old". Use an f-string in your solution to this problem.
birth = int(input("What year were you born? "))
current = int(input("What year is it right now? "))
age = current - birth
print(f"You are {age} years old if you have already had your birthday this year!")
