"""
Ths module lists out all framework available for selection
"""


def select_framework():
    """ Framework Selection """

    frameworks = 'Flask'

    select = input('Enter Framework:')

    if select == frameworks:
        print("You have selected Flask framework")
