import random
import string


class DataHelper:
    @staticmethod
    def generate_name():
        name_length = random.randint(3, 6)
        name = ''.join(
            random.choice(string.ascii_letters)
            for _ in range(name_length)
        )

        return name

    @staticmethod
    def generate_login():
        digits = ''.join(random.choices(string.digits, k=3))

        domains = ['ya.ru', 'gmail.com', 'mail.ru', 'yandex.ru']
        domain = random.choice(domains)

        return f'kirill_tolokonnikov_22_{digits}@{domain}'.lower()

    @staticmethod
    def generate_password(min_length=6, max_length=12):
        length = random.randint(min_length, max_length)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))

        return password
