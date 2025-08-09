print("Lesson 3. Home task №6.")
"""
Дано целое число. Выведите его последнюю цифру.
Например, дано 200 - последняя цифра 0. Дано 123 - последняя
цифра 3. Дано 587 - последняя 7.
"""

try:
    integer_number = int(input("Enter a integer number: "))
    print("Entered number is: ",  integer_number)
    print(" ")
    print("The last digit of the entered number is", str(integer_number)[-1])

except  ValueError:
    print("You have entered the line or a number with a comma!!!")
