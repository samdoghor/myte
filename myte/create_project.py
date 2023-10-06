# create_project.py

"""
This module defines all functions and classes to create the boilerplate.
"""

import os
import shutil

import inquirer
import typer
from rich import print as mprint
from rich.prompt import Prompt


class CreateProject:
    """ This class defines the project creation """

    @staticmethod
    def project_setup():
        """ This function defines the project creation """

        # create directory
        def create_dir(project_name):
            """ This function defines the creation of directory """

            project_folder = os.path.abspath(f"{project_name}")
            create_dir = shutil.copytree(template_folder, project_folder)
            mprint("[blue]Successful[/blue]")

            mprint(f"""
[yellow]Usage:[/yellow]
- cd into {project_name}

- pip install virtualenv (if not installed)

- create a virtual environment
    [magenta]* windows: virtualenv env
    * linux: python3 -m virtualenv env[/magenta]

- activate virtual environment
    [magenta]* windows: source .env/scripts/activate
    * linux: source .env/bin/activate[/magenta]

- run `pip install -r requirements`
""")

            return create_dir

        # delete directory
        def delete_dir(project_name):
            """ This function defines the deletion of directory to override """

            if os.path.exists(project_name):
                mprint(
                    f"[red]Folder '{project_name}' already exists.[/red]")
                confirmation = typer.confirm("Do you want to override existing files?")  # noqa

                if not confirmation:
                    mprint("[red]The programme will now terminate[/red] [blink][/blink]")  # noqa
                    raise typer.Abort()

                delete_dir = shutil.rmtree(os.path.abspath(f"{project_name}"))

                return delete_dir

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

            if selected_framework['framework'] == "Flask":  # noqa
                if selected_setup['setup'] == "Simple":
                    delete_dir(project_name)
                    template_folder = os.path.abspath("../personals/myte/myte/templates/template-flask-simple")  # noqa
                    create_dir(project_name)

                if selected_setup['setup'] == "Moderate":  # noqa
                    delete_dir(project_name)
                    template_folder = os.path.abspath("../personals/myte/myte/templates/template-flask-moderate")  # noqa
                    create_dir(project_name)

                if selected_setup['setup'] == "Robust":  # noqa
                    delete_dir(project_name)
                    template_folder = os.path.abspath("../personals/myte/myte/templates/template-flask-robust")  # noqa
                    create_dir(project_name)
