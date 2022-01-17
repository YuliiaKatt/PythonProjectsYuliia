import random

# Программа вычисляет количество чисел, которые больше своих сосдей в списке

# Генерируем список из 10 чисел
list_numbers = [random.randint(0, 100) for i in range(10)]
print(list_numbers)

count_max = 0

# Сравниваем соседние элементы списка и считаем количество максимальных значений (без учета крайних чисел)
for i in range(1, len(list_numbers) - 1):
    if list_numbers[i] > list_numbers[i - 1] and list_numbers[i] > list_numbers[i + 1]:
        count_max += 1
print("Количество чисел, которые больше своих сосдей: ", count_max)
