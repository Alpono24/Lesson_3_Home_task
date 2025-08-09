print("Lesson 3. Home task №8.")
"""
Дано трехзначное число, найти сумму его цифр. 
Например, дано 123 – сумма 6, дано 555, сумма 15.
"""
try:
    three_digit_number = int(input("Enter a three-digit number: "))
    if len(str(three_digit_number)) == 3:
        print("The sum of the digits of the entered number is:",
              int(str(three_digit_number)[0]) + int(str(three_digit_number)[1]) + int(str(three_digit_number)[2]))
    elif len(str(three_digit_number)) < 3 or len(str(three_digit_number)) > 3:
        print("The entered number is NOT three digits!!!")
except  ValueError:
    print("You have entered the line or a number with a comma!!!")
