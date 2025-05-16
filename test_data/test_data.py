from attr import dataclass


@dataclass
class UserData:
    name: str = 'Кирилл'
    email: str = 'kirill_tolokonnikov_22_1997@gmail.com'
    password: str = '1234qwer'
