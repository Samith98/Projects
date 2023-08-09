import random
import string
import re

PASSWORD_LENGTH = random.randrange(13, 16)
PASSWORD_CHAR_LENGTH = 10
PASSWORD_SPC_LENGTH = random.randrange(1, 3)
PASSWORD_DIGIT_LENGTH = PASSWORD_LENGTH - PASSWORD_CHAR_LENGTH - PASSWORD_SPC_LENGTH

if __name__ == '__main__':
    password_char_univ = string.ascii_lowercase + string.ascii_uppercase
    special_char = "@#$%!=:?~>*()<"
    digit = string.digits
    password = []
    for _ in range(PASSWORD_CHAR_LENGTH):
        password.append(random.choice(password_char_univ))
    random.shuffle(password)
    for _ in range(PASSWORD_SPC_LENGTH):
        password.append(random.choice(special_char))
    random.shuffle(password)
    for _ in range(PASSWORD_DIGIT_LENGTH):
        password.append(random.choice(digit))
    while True:
        if re.search("^[a-zA-Z]", "".join(password)) and  not re.search(".*[\d]$", "".join(password)):
            break
        random.shuffle(password)
    password = "".join(password)
