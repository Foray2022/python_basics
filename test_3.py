# Задание
#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#Решение
n = int(input('Enter a number from 0 to 9еуы:'))
temp = str(n) #переводим число в строковый формат
temp_1 = temp + temp #выполняем конкатенацию строк
temp_2 = temp + temp_1
print("The result is equal to:",n ,'+', temp_1, '+', temp_2, '=',n + int(temp_1) + int(temp_2))

