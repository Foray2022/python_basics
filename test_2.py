#Задание
#Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Решение
print('Enter the time in seconds')
time = input("Time: ")

try:
    time = int(time)
    print("TIME:", time//3600, ':', time%3600//60, ':', time%60 )
    #Часы time//3600 минуты time%3600//60 секунды time%60
except ValueError:#обработка исключений
    print('Incorrect input')