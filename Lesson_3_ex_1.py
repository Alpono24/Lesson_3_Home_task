print("Lesson 3. Home task №1.")
""" 
Eсть три целочисленные переменные, нужно посчитать:
● сумму
● разность
● произведение
● от первой переменной отнять вторую и прибавить третью
● поделить произведение двух переменных на третью
● от суммы первых двух переменных найти остаток от деления на третью переменную
"""
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
print("Entered numbers are: ", first_number, " ,", second_number, " ,", third_number)
print(" ")
print("The sum of three numbers is equal to: ", first_number + second_number + third_number)
print("The difference of three numbers is equal to: ", first_number - second_number - third_number)
print("The product of three numbers is equal to: ", first_number * second_number * third_number)
print("The first number minus the second number and plus the third number is equal to: ", first_number - second_number + third_number)
print("The result of dividing the product of two numbers by the third number is equal to: ", (first_number * second_number) / third_number)
print("The remainder of dividing the sum of the first two numbers by the third is equal to: ", (first_number + second_number) % third_number)