from functools import reduce

def checkio(number):
    """
    Функция убирает из введенного пользователем числа "0".
    Извлекает цифры из числа (переводя введенную строку в список)
    Вычисляет произведение всех цифр.
    :param number: введенное пользователем число
    :return: произведение всех цифр числа
    """
    multiply_number = [int(i) for i in str(number).replace("0", "")]
    return reduce(lambda x, y: x * y, multiply_number)


def main():
    input_number = int(input("Введите положительное целое число = "))
    print("Произведение всех цифр числа (за исключением нулей) = ", checkio(input_number))


if __name__ == "__main__":
    main()
