def arithmetic(number1, number2, operator):
    """
    Функция выполняет математические операции (сложение, вычитание, умножение и деление) над двумя числами.
    :param number1: первое число
    :param number2: второе число
    :param operator: операция, которая должна быть произведена над числами (+, -, *, /)
    :return: результаты математических вычислений либо строка "Неизвестная операция"
    """
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    return "Неизвестная операция"


def main():
    number_1 = int(input("Введите первое число = "))
    number_2 = int(input("Введите второе число = "))
    operation = input("Введите знак +, -, *, /  ")
    print(f"{number_1} {operation} {number_2} = ", arithmetic(number_1, number_2, operation))


if __name__ == "__main__":
    main()
