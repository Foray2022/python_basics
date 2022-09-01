#Задание
#Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

#Решение
profit = float(input('Enter the profit value:'))#Значение выручки
cost = float(input('Enter the cost value:'))#Значение издержек
if profit > cost:#Если выручка больше издержек
    print("Profit is more than costs")
else:#Иначе
    print("loss — costs are more than revenue")