from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'Only letters. First letter is uppercase. Max length is 20 characters.'
    )

    PASSWORD = (

        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$',
        [
            'password must contain 1 number(0 - 9)',
            'password must contain 1 uppercase letters',
            'password must contain 1 lowercase letters',
            'password must contain 1 non - alpha numeric number',
            'password is 8 - 16 characters with no space',

        ]
    )
    BRAND_NAME = (
        '^(?!.*\s)[A-Z][a-z]{1,49}(?<!\s)$',
        [
            'First letter of brand must be only uppercase letters.',
            'Not aloud spaces at the beginning or end of the brand.',
            'Second letter of brand must be only lowercase letters.',
            'Length of brand must be between 3 and 50 characters.',
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
