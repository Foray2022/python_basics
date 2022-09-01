# Задание
# (Дополнительно). Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# Решение
primary_result = float(input('Enter the result of the first run:'))  # результат первой пробежки
desired_result = float(input('Enter the desired result of the run:'))  # искомый результат пробежки
day = 1  # cчетчик дней
intermediate_result = primary_result  # переменная для промежуточного результата
print('Day', day, ":", intermediate_result)
while intermediate_result <= desired_result:  # пока результат пробежки не станет больше или равен предельному результату
    intermediate_result += intermediate_result * 0.1  # увеличение результата пробежки на 10%
    day += 1  # инкремент счетчика дней
    print('Day', day, ":", intermediate_result)
print("You will achieve the required indicators on", day, "day")
