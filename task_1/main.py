# Арсений Жук

# объявляем список строк
strs = ["Loremд", "ipsдum", "dolor", "sit", "amet", "consectetur"]

# объявляем счетчик
counter = 0

for word in strs: # бежим по списку строк, берем строку
    for letter in word: # бежим по символам строки
        if letter == "д": # если символ д, то увеличиваем счетчик
            counter += 1
            break # выходим из цикла
            
print("Количество строк с буквой д:", counter) # выводим счетчик