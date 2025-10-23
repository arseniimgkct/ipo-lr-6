# Арсений Жук
import random

values = [-3, -5, -2, -12, 0, 15 ,4, 7, 2] 

n, m = random.randint(4, 8), random.randint(4, 8)

# создаём матрицу высотой n, шириной m, заполняя её случайными элементами из values
matrix = [[random.choice(values) for _ in range (m)] for _ in range(n)]

print("Матрица")
for i in range(n): # бежим по высоте
    for j in range(m): # бежим по строке
        print(matrix[i][j], end=" ") # выводим элемент по индексу i j
    print() # выводим пустую строку
print() # выводим пустую строку

# считаем сумму всех отрицательных элементов матрицы
negative_sum = sum(x for row in matrix for x in row if x < 0)

print("Сумма всех отрицательных элементов:", negative_sum) # выводим сумму отрицательных чисел