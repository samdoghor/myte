# errors.py

"""
This module defines functions to tackle errors encountered.
"""


class UKeyboardInterrupt(Exception):
    """ This class represents Keyboard Interruption """

    def __init__(self) -> None:
        self.exception = KeyboardInterrupt
        self.type = 'Keyboard Interrupt'
        self.message = 'Programme terminated because a Termination Key was hit by the user'  # noqa
