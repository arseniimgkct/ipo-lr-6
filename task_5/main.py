# Арсений Жук

import random # импортируем модуль рандом

random_numbers = [random.randint(-50, 50) for _ in range(0, 25)] # генерируем список рандомных значений

negative, positive, zero = 0, 0, 0 # объявляем счетчики отрицательных, положительных, нулевых элементов

for num in random_numbers: # бежим по рандомным числам
    if num > 0: # если положительное
        positive += 1 # увеличиваем счетчик положительных
    elif num < 0: # если отрицательное
        negative += 1 # увеличиваем счетчик отрицательных
    else: # иначе
        zero += 1 # увеличиваем счетчик нулей
        
print(f'Положительных {positive}: {positive / len(random_numbers) * 100:g}%') # выводим в консоль
print(f'Отрицательных {negative}: {negative / len(random_numbers) * 100:g}%') # выводим в консоль
if zero != 0: # если нулей больше 0
    print(f'Нулей {zero}: {zero / len(random_numbers) * 100:f}%') # выводим кол-во
else :
    print("Нулей: 0") # выводим что нулей 0