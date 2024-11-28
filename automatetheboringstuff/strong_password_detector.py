"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength.
"""

import re


def is_strong_password(password):
    length_regex = re.compile(r'.{8,}')

    lowercase_regex = re.compile(r'[a-z]')

    uppercase_regex = re.compile(r'[A-Z]')

    digit_regex = re.compile(r'\d')

    if (length_regex.search(password) and
        lowercase_regex.search(password) and
        uppercase_regex.search(password) and
        digit_regex.search(password)):
        return True
    else:
        return False
