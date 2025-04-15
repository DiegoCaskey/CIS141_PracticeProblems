# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num_1 = float(input("Give me a number: "))
num_2 = float(input("Give me another number: "))
answer_1 = num_1 + num_2
answer_2 = num_1 - num_2
answer_3 = num_1 * num_2
answer_4 = num_1 / num_2
print(f"{num_1} plus {num_2} equals {answer_1}")
print(f"{num_1} minus {num_2} equals {answer_2}")
print(f"{num_1} times {num_2} equals {answer_3}")
print(f"{num_1} divided by {num_2} equals {answer_4:.3f}")
