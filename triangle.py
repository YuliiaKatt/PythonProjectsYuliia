# Программа рисует фигуру D (ромб c полосой посередине)

# Пользователь вводит с клавиатуры высоту фигуры
height_picture = int(input("Введите высоту рисунка (нечетное число): "))

# Делаем рисунок симметричным. Если пользователь введет четное число, то рисунок увеличится на 1 символ
if height_picture % 2 == 0:
    height_picture += 1

# Ромб будет состоять из треугольников, где высота треугольников
height_triangle = int(height_picture / 2) + 1

# Ширина треугольников
length_triangle = height_picture

# Символы, которыми будет нарисована картинка
star = "* "
space = "  "

# Рисуем первый треугольник (заполненный "*")
for i in reversed(range(height_triangle)):
    picture1 = space * i + star * (length_triangle - i * 2) + space * i
    print(picture1)

# Рисуем второй треугольник
for i in range(height_triangle):
    picture2 = space * i + star * (length_triangle - i * 2) + space * i
    #  Пропускаем первую итерацию, чтоб не выводилось основание второго треугольника
    if i == 0:
        continue
    #  Делаем треугольник пустым, с полосой посередине
    elif i != (height_triangle - 1):
        half_line = int((length_triangle - 2 - i * 2) / 2)
        picture3 = space * i + star + space * half_line + star + space * half_line + star + space * i
        print(picture3)
    else:
        print(picture2)
