# setup_project.py

"""
This module defines functions to create the boilerplate.
"""

import inquirer
from create_project import CreateProject
from delete_project import DeleteProject
from rich import print as mprint
from rich.prompt import Prompt


class SetupProject:
    """ This class defines the project creation """

    @staticmethod
    def project_setup():
        """ This function defines the setup for the biolerplate creation """

        # get project name
        project_name = Prompt.ask(
            "Project Name", default="myte-project")

        mprint(f"[green]✅[/green] Project name: {project_name}")

        # get framework choice
        frameworks_choice = ["Flask", "Flask-Restful-API"]
        frameworks = [
            inquirer.List(
                "framework",
                message="Select a framework",
                choices=frameworks_choice,
                carousel=True,
            )
        ]
        selected_framework = inquirer.prompt(frameworks)

        mprint(f"[green]✅[/green] {selected_framework['framework']},  selected")  # noqa

        # get setup choice
        setup_choice = ["Simple", "Moderate", "Robust"]
        setups = [
            inquirer.List(
                "setup",
                message="Select a framework",
                choices=setup_choice,
                carousel=True,
            )
        ]
        selected_setup = inquirer.prompt(setups)

        mprint(f"[green]✅[/green] {selected_setup['setup']},  selected")  # noqa

        # boilerplate execution
        if project_name and selected_framework['framework'] and selected_setup['setup']:  # noqa

            if project_name == ".":
                DeleteProject.delete_files()
                CreateProject.create_files(selected_framework, selected_setup)  # noqa
            else:
                DeleteProject.delete_dir(project_name)
                CreateProject.create_dir(project_name, selected_framework, selected_setup)  # noqa
