import random, string

# Создаем словарь 1, где случайные маленькие буквы - это ключи, а случайные числа - это значения
dict1 = {random.choice(string.ascii_lowercase): random.randint(0, 10) for i in range(10)}
print(dict1)

# Создаем словарь 2, где случайные маленькие буквы - это ключи, а случайные числа - это значения
dict2 = {random.choice(string.ascii_lowercase): random.randint(0, 10) for j in range(10)}
print(dict2)

# Обьединяем словари и получаем общий словарь, в котором значения одинаковых ключей заменяются значениями со словаря 2
dict3 = {**dict1, **dict2}

# Если максимальные значения повторяющихся ключей все-таки находятся в словаре 1, тогда
# заменяем в общем словаре одинаковые ключи максимальными значения со словаря 1
dict3.update({k: dict1[k] for k in dict1 if k in dict2 and dict1[k] > dict2[k]})
print(dict3)

