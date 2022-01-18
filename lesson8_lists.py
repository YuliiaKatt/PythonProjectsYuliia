import random
# Генерируем список 1
list1 = [random.randint(0, 10) for i in range(5)]
print(list1)

# Генерируем список 2
list2 = [random.randint(0, 10) for j in range(5)]
print(list2)

# Создаем список уникальных чисел
unique = []

# Складываем списки. Когда число в списке встречается только один раз, мы добавляем его в новый список
# и выводим длину списка, которая равна количеству уникальных чисел.
print("Количество уникальных чисел ")
print(len([unique.append(i) for i in (list1 + list2) if (list1+list2).count(i) == 1]))
