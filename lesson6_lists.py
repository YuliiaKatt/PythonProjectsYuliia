import random

# Программа определяет по росту, на каком месте в строю должен стоять ученик Петя
x = int(input("Введите рост Пети: "))

students = int(input("Введите количество учеников в классе: "))

# Генерируем список из параметров роста учеников
height_students = [random.randint(150, 200) for i in range(students)]
print("Список учеников:\n", height_students)

# Добавляем Петю в список учеников
height_students.append(x)

# Отсортировываем список роста учеников по убыванию
height_students.sort(reverse=True)
print("Список учеников (вместе с Петей), отсортированных по росту:\n", height_students)

# Определяем место в строю для Пети
any([x in height_students])
print("Петя должен встать в строй под номером: ", students - height_students[::-1].index(x) + 1)
