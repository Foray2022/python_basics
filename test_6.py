#Задание
#Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

#Решение
profit = float(input('Enter the profit value:'))#Значение выручки
cost = float(input('Enter the cost value:'))#Значение издержек
if profit > cost:#Если выручка больше издержек
    print(f"Profit is more than costs {profit / cost:.2f}")#Выводим значение рентабельности выручки
    number_staff = int(input("Enter the number of employees of the company "))#Запрос количества сотрудников фирмы
    print(f"The profit per employee was {profit / number_staff:.2f}")#Прибыль фирмы в расчете на одного сотрудника
else:#Иначе
    print("loss — costs are more than revenue")