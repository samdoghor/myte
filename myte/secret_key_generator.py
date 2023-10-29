# secret_key_generator.py

"""
This module generates secret keys to used in the frameworks templates
"""


import secrets
import string


class GenerateSecretKey:
    """ This class is use to generate secret key to be used for security
    purposes """

    def generate_secret_key(length=32):
        """ The function generates a 32 character secret key """

        alphabet = string.ascii_letters + string.digits
        secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
        return secret_key
