import random
import string


def random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_email(domain="@yandex.ru", username_length=8):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return username + domain