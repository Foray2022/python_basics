#Задание
#Поработайте с переменными, создайте несколько, выведите на экран.
#Запросите у пользователя некоторые числа и строки и сохраните в переменные,
#затем выведите на экран
#Решение

first_sting = 'The first Task'
print(first_sting)
first_number = 1
print(first_number)
txt = input('Enter a string or number:')#Переменная для хранения введенных данных
print('Enterid date:', txt)
txt = input("Enter number: ")
try:#проверка на корректность ввода
    number = int(txt)# Переменная для хранения введеного числа
    print('Enterid number:', number)
except ValueError:#обработка исключений
    print(" This is the line try again.")