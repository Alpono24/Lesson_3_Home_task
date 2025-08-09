print("Lesson 3. Home task №3.")
"""
Дана строка, состоящая из слов, разделенных пробелами. (Вот 4
варианта тестовых данных для программы: ‘Hello world’, ‘a b c’, ‘test’,
‘test1 test2 test3 test4 test5’). Определите, сколько в ней слов.
"""

str = input("Enter a string: ")
print("You have entered the following line: ", str)
print("There are", str.count(" ")+1, "words in your line.", )
