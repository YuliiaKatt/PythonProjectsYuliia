# Программа рисует фигуру С (ромб)
# Пользователь вводит с клавиатуры высоту фигуры
height_picture = int(input("Введите высоту рисунка: "))

# Ширина рисунка
length_picture = height_picture

# Ромб будет состоять из треугольников, где высота треугольников
height_triangle = int(height_picture / 2) + 1

# Символы, которыми будет нарисована картинка
star = "* "
space = "  "

# Первый треугольник
for i in reversed(range(height_picture)):
    picture1 = space * i + star * (length_picture - i * 2) + space * i
    print(picture1)

# Второй треугольник
for i in range(height_picture):
    i += 1
    picture2 = space * i + star * (length_picture - i * 2) + space * i

    # if i == 0:
    #     continue
    elif i != (height_picture - 1):
        picture3 = space * i + star + space * ((length_picture - 2) - i * 2) + star + space * i
        print(picture3)
    # elif i == (length_picture - height_picture):
    #     print(star)

    else:
        print(picture2)