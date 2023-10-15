# delete_project.py

"""
This module defines delete/override function for .
"""

import os
import shutil

import typer
from rich import print as mprint


class DeleteProject:
    """ This class defines the project deletion/override function """

    @staticmethod
    def delete_dir(project_name):
        """ This function defines the deletion/override of a directory  """

        if os.path.exists(project_name):
            mprint(
                f"[red]Folder '{project_name}' already exists.[/red]")

            confirmation = typer.confirm("Do you want to override existing files?")  # noqa

            if not confirmation:
                mprint("[red]The programme will now terminate[/red] [blink][/blink]")  # noqa
                raise typer.Abort()

            shutil.rmtree(os.path.abspath(f"{project_name}"))
