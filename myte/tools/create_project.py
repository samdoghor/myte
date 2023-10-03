# tools.py

"""
This module defines all functions and classes to create the boilerplate.
"""

import time
import inquirer
from rich import print as mprint
from rich.prompt import Prompt

from .flask_framework import FlaskFramework


class CreateProject:
    """ This class defines the project creation """

    @staticmethod
    def create_project():
        """ This function defines the project creation """

        project_name = Prompt.ask(
            "Project Name", default="myte-project")

        mprint(f"""
[green]✅[/green] Project name: {project_name}
        """)

        time.sleep(2)

        frameworks_choice = ["Flask", "Bottle", "Web2py"]

        frameworks = [

            inquirer.List(
                "framework",
                message="Select a framework",
                choices=frameworks_choice,
                carousel=True,  # Enables arrow key navigation
            )
        ]

        selected_framework = inquirer.prompt(frameworks)

        mprint(f"""
[green]✅[/green] {selected_framework['framework']},  selected
        """)

        time.sleep(2)

        if selected_framework['framework'] == "Flask":
            FlaskFramework.flask_project()
