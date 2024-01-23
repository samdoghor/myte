# secret_key_generator.py

"""
This module generates secret keys to used in the frameworks templates
"""


import secrets


class GenerateSecretKey:
    """ This class is use to generate secret key to be used for security
    purposes """

    def generate_secret_key():
        """ The function generates a 32 character secret key """

        length = 32
        secret_key = secrets.token_urlsafe(length)

        return secret_key
