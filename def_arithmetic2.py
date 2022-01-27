def arithmetic2(number1, number2, operator):
    """
    Функция выполняет математические операции (сложение, вычитание, умножение и деление) над двумя числами.
    Для этого создаем словарь, где ключи - это операторы (+, -, *, /), а значения ключей - это действия над числами.
    :param number1: первое число
    :param number2: второе число
    :param operator: операция, которая должна быть произведена над числами (+, -, *, /)
    :return: значение ключа (результаты математических вычислений) либо строка "Неизвестная операция"
    """
    d = {"+": number1 + number2, "-": number1 - number2, "*": number1 * number2, "/": number1 / number2}
    return d.get(operator, "Неизвестная операция")


def main():
    number_1 = int(input("Введите первое число = "))
    number_2 = int(input("Введите второе число = "))
    operation = input("Введите знак +, -, *, /  ")
    print(f"{number_1} {operation} {number_2} = ", arithmetic2(number_1, number_2, operation))


if __name__ == "__main__":
    main()
