import random
import string


def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()"

    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(symbols)]

    all_chars = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)

    return "".join(password)