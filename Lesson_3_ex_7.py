print("Lesson 3. Home task №7.")
"""
Дано трехзначное число, найти количество его десятков.
Например, дано 123 – количество десятков: 2, дано 978 –
количество десятков: 7
"""

try:
    three_digit_number = int(input("Enter a three-digit number: "))
    if len(str(three_digit_number)) == 3:
        print("The number of tens of the entered number is:", str(three_digit_number)[1])
    elif len(str(three_digit_number)) < 3 or len(str(three_digit_number)) > 3:
        print("The entered number is NOT three digits!!!")
except  ValueError:
    print("You have entered the line or a number with a comma!!!")
