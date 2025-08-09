print("Lesson 3. Home task №4.")
"""
Дана строка. Замените в этой строке все появления буквы h на
букву H, кроме первого и последнего вхождения.
Подсказка: использовать метод replace с параметрами.
Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’
"""


str = input("Enter a string: ")
print("You have entered the following line: ", str)
print("The result of the changes: ", str[0]+str[1:-1].replace("h", "H")+str[-1])

