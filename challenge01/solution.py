import re

REQUIRED_DATA = ["usr:", "eme:", "psw:", "age:", "loc:", "fll:"]
END_LINE = "\n"


def split_into_users(data: list[str]):
    users: list[str] = []
    current_user: str = ""
    for line in data:
        if line is not END_LINE:
            current_user += line
        else:
            users.append(current_user)
            current_user = ""
    return users


def validate_user(user: str):
    for req_data in REQUIRED_DATA:
        if req_data not in user:
            return False
    return True


def get_username(user: str):
    return re.split(f"[ |{END_LINE}]", user.split(REQUIRED_DATA[0])[1])[0]


with open("users.txt", "r") as file:
    users_quantity = 0
    last_username = ""
    for user in split_into_users(file.readlines()):
        if validate_user(user):
            users_quantity += 1
            last_username = get_username(user)
    print(users_quantity, last_username, sep="")
