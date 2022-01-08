user_word = input("Введите любую строку, слово или число: ")

# Вставка слова (введенного с клавиатуры) в строку
new_string = f"Это строка в которую {user_word} новую строку"
print(new_string)

# Замена слова в строке (введенного с клавиатуры), на фразу "замена в строке"
replace_string = new_string.replace(f"{user_word}", "замена в строке")
print(replace_string)

# Вывод на экран длинны строки
print(len(replace_string))

# Проверка, есть ли в строке слово "строка" и вывод на экран ответа - Да или НЕТ
keyword = "строка"
if keyword in replace_string:
    print("Да")
else:
    print("Нет")
