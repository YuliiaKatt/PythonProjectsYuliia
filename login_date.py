import datetime

dict_password = {"a": "1111", "b": "2222", "c": "3333"}

n_minutes = 5


def authenticate(user) -> bool:
    """
    The function blocks the program for (n_minutes) minutes in case of incorrectly entered login
    :return: bool
    """
    for key,value in save_last_fail_login().items():
        if key == user and value > datetime.datetime.now() - datetime.timedelta(minutes=n_minutes):
            print(f"Вы заблокированы! Следующая попытка через {n_minutes} минут")
            exit()
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
        if not authenticate(user_main):
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


def try_enter():
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


def save_last_fail_login():
    """
    The function saves the time of the last incorrectly entered login
    :return: datetime
    """
    date = datetime.datetime.now() - datetime.timedelta(minutes=n_minutes - 1)
    dict_fail_password = dict.fromkeys(dict_password, date)
    return dict_fail_password


def main():
    """
     The fanction describe the actions after the user types in console correct or incorrect username and password,
     or if the user types in console only one argument (username or password).
    :return:
    """
    params = parse_args()

    if login(params.username or input("Enter your name: "), params.password or input("Enter your password: ")) is True:
        print("Вы в системе!")
    else:
        try_enter()


if __name__ == "__main__":
    main()
