import pytest
import random
import string


@pytest.fixture
def random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))

@pytest.fixture
def random_email():
    domain = "@yandex.ru"
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return username + domain