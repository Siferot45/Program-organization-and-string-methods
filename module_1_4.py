my_string = input("Введите строку с произвольным текстом: ")

print("Количество символов в введённом тексте: ", len(my_string))

print("Строка в верхнем регистре: ", my_string.upper())
print("Строка в верхнем регистре: ", my_string.lower())

print("Строка без пробелов: ", my_string.replace(" ", ""))

print(my_string[0])
print(my_string[-1])