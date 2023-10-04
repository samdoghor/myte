# create_project.py

"""
This module defines all functions and classes to create the boilerplate.
"""

import shutil
import os
import inquirer
from rich import print as mprint
from rich.prompt import Prompt
import typer


class CreateProject:
    """ This class defines the project creation """

    @staticmethod
    def project_setup():
        """ This function defines the project creation """

        # project name
        project_name = Prompt.ask(
            "Project Name", default="myte-project")

        mprint(f"[green]✅[/green] Project name: {project_name}")

        # framework choice
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

        # setup choice
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

        if project_name and selected_framework['framework'] and selected_setup['setup']:  # noqa
            if selected_framework['framework'] == "Flask" and selected_setup['setup'] == "Simple":  # noqa
                if os.path.exists(project_name):
                    mprint(
                        f"[red]Folder '{project_name}' already exists.[/red]")

                    confirmation = typer.confirm("Do you want to override existing files?")  # noqa

                    if not confirmation:
                        mprint("[red]The programme will now terminate[/red] [blink][/blink]")  # noqa
                        raise typer.Abort()

                    shutil.rmtree(os.path.abspath(f"{project_name}"))

                template_folder = os.path.abspath("myte/myte/templates/template-flask-simple")  # noqa
                project_folder = os.path.abspath(f"{project_name}")
                shutil.copytree(template_folder, project_folder)

                mprint("[blue]Successful[/blue]")
