# create_project.py

"""
This module defines the functions that create the boilerplate.
"""

import os
import shutil

from constants import current_dir, template_folder
from rich import print as mprint


class CreateProject:
    """ This class defines the boilerplate creation """

    @staticmethod
    def create_dir(project_name, selected_setup):
        """ This function defines the creation of directory """

        source_folder = os.path.join(template_folder,
                                        f"template-flask-{selected_setup['setup']}")  # noqa
        destination_folder = os.path.join(current_dir, project_name)
        shutil.copytree(source_folder, destination_folder)

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
"""
               )
