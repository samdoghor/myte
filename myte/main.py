# main.py

"""
This module is the entry point of the application.
All configurations are done here.
"""

import typer
from constants import messages
from rich import print as mprint
from rich.console import Console
from rich.text import Text

from setup_project import SetupProject

# cli initialization

myte = typer.Typer()


# cli start point


@myte.command()
def main():
    """ The defines myte main function """

    console = Console()

    mprint("[yellow]Compatible Note:[/yellow]")
    mprint(Text(messages["welcome"], "green").wrap(console, 70))
    mprint(messages["salutations"]["thank_you"])
    mprint("\n")

    confirmation = typer.confirm(messages["warnings"]["start_confirmation"])
    mprint("\n")

    if not confirmation:
        mprint(messages["warnings"]["program_termination"])

        raise typer.Abort()

    SetupProject.project_setup()


# app run
if __name__ == "__main__":
    myte()
