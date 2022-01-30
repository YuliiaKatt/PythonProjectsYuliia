def authenticate() -> bool:
    """

    :return: bool
    """
    return True


def check_password(username: str, password: str) -> bool:
    """
    The function returns True if the pair (username, password) matches the pair (key, value)
    in the global dictionary.
    :param username: str
    :param password: str
    :return: bool
    """
    return (username, password) in dict_password.items()


def decorator(func):
    def wrapper(user_main, password_main):
        if not check_password(user_main, password_main):
            return False
        if not authenticate():
            return False
        return func(user_main, password_main)
    return wrapper

@decorator
def login(username: str, password: str) -> bool:
    """

    :param username: str
    :param password: str
    :return: bool
    """
    return True


def main():
    """
    The function describes the actions after the user enters a username and password.
    If the username and password are correct, print "Вы в системе!"
    If  the username and password are incorrect, print "Неправильное Имя или Пароль. У вас осталось N попыток"
    The user has 3 attempts to enter the correct password.
    :return: None
    """
    count = 3
    while count >= 0:
        if count == 0:
            print("Попытки истекли!")
            break
        user_new = input("Enter your name: ")
        password_new = input("Enter your password: ")
        if login(user_new, password_new) is False:
            count -= 1
            print(f"Неправильное Имя или Пароль. У вас осталось {count} попыток")
        else:
            print("Вы в системе!")
            break


if __name__ == "__main__":
    dict_password = {"1111": "1111", "2222": "2222", "3333": "3333"}
    main()
