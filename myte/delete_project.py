# delete_project.py

"""
This module defines delete/override function for .
"""

import os
import shutil

import typer
from constants import current_dir, messages
from rich import print as mprint


class DeleteProject:
    """ This class defines the project deletion/override function """

    @staticmethod
    def delete_dir(project_name):
        """ This function defines the deletion/override of a directory  """

        if os.path.exists(project_name):
            mprint(messages["warnings"]["dir_exist"])

            confirmation = typer.confirm(messages["warnings"]["deletion_warning"] + "[blink][/blink]")  # noqa

            if not confirmation:
                mprint(messages["warnings"]["program_termination"] + "[blink][/blink]")  # noqa
                raise typer.Abort()

            confirmation_yes = typer.confirm(messages["warnings"]["deletion_confirmed"])  # noqa

            if not confirmation_yes:
                mprint(messages["warnings"]["program_termination"] + "[blink][/blink]")  # noqa
                raise typer.Abort()

            shutil.rmtree(os.path.abspath(f"{project_name}"))

            mprint("[blue]" + messages["success"]
                   ["override_success"] + "[/blue]")

    @staticmethod
    def delete_files():
        """ This function defines the deletion/override of a file(s)  """

        current_files = os.listdir(current_dir)

        if current_files:
            mprint(messages["warnings"]["not_empty_dir"])

            confirmation = typer.confirm(messages["warnings"]["deletion_warning"] + "[blink][/blink]")  # noqa

            if not confirmation:
                mprint(messages["warnings"]["program_termination"] + "[blink][/blink]")  # noqa
                raise typer.Abort()

            confirmation_yes = typer.confirm(messages["warnings"]["deletion_confirmed"])  # noqa

            if not confirmation_yes:
                mprint(messages["warnings"]["program_termination"] + "[blink][/blink]")  # noqa
                raise typer.Abort()

            for file in os.listdir(current_dir):
                source_path = os.path.join(current_dir, file)

                if os.path.isfile(source_path):
                    os.remove(source_path)
                elif os.path.isdir(source_path):
                    shutil.rmtree(source_path)

            mprint("[blue]" + messages["success"]
                   ["override_success"] + "[/blue]")
