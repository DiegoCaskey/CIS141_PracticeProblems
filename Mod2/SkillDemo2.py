name = input("What is your name? ")
price = float(input("How much is the meal? "))
members = int(input("How many people are splitting the bill? "))
total = price / members
print(f"Ok {name}, each member will pay ${total:.2f}!")
