# Арсений Жук

text = input("Введите строку для поиска: ") # получаем строку для поиска

founded = [] # объявляем пустой массив

with open("text.txt", "r", encoding="utf-8") as file: # открываем файл кодировкой utf-8 только для чтения
    for line in file: # бежим по строкам
        if text in line: # если в строке содержится исходное слово
            founded.append(line) # то добавляем его в founded
            continue # переходим к следующей строке
        
founded.sort(key=lambda s: len(s)) # сортируем их по длине 

for s in founded: # выводим
    print(s)