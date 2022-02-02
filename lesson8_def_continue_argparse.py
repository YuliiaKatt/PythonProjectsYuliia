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

def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--username", action="store")
    parser.add_argument("--password", action="store")

    return parser.parse_args()

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
        print(f"Неправильное Имя или Пароль. У вас осталось {count} попыток")
        user_new = input("Enter your name: ")
        password_new = input("Enter your password: ")
        if login(user_new, password_new) is False:
            count -= 1
        else:
            print("Вы в системе!")
            break


if __name__ == "__main__":
    # Password database
    dict_password = {"a": "1111", "b": "2222", "c": "3333"}

    params = parse_args()

    dict_params = {params.username: params.password}

    for i in dict_params:
        for j in dict_password:

            # If the user enters the correct login details
            if i == j and dict_params[i] == dict_password[j]:
                print("Вы в системе!")
                break

            # If the user enters only username
            if i == j and dict_params[i] is None:
                user_main = params.username
                password_main = input("Введите ваш пароль: ")
                if login(user_main, password_main) is False:
                    main()
                    break
                else:
                     print("Вы в системе!")
                     break

            # If the user enters only password
            elif i is None and dict_params[i] == dict_password[j]:
                user_main = input("Введите ваше имя: ")
                password_main = dict_params[i]
                if login(user_main, password_main) is False:
                    main()
                    break
                else:
                     print("Вы в системе!")
                     break

            # If the user enters the wrong login details
            if i not in dict_password or dict_params[i] not in dict_password:
                main()
                break
