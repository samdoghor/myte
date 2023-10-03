# tools.py

"""
This module defines all functions and classes to create the boilerplate.
"""

import inquirer
from rich import print as mprint


class FlaskFramework:
    """ This class defines the project creation """

    @staticmethod
    def flask_project():
        """ This function defines the project creation """

        flask_choice = ["Regular", "API"]

        flask = [

            inquirer.List(
                "flask",
                message="Select what you want to build",
                choices=flask_choice,
                carousel=True,  # Enables arrow key navigation
            )
        ]

        selected_flask = inquirer.prompt(flask)

        mprint(f"""
[green]✅[/green] {selected_flask['flask']},  selected
        """)
