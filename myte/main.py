# main.py

"""
This module is the entry point of the application.
All configurations are done here.
"""

import typer
from rich import print as mprint
from setup_project import SetupProject
from constants import messages

# cli initialization

myte = typer.Typer()


# cli start point


@myte.command()
def main():
    """ The defines myte main function """

    mprint("[yellow]Compatible Note:[/yellow]")
    mprint(messages["welcome"])
    mprint("[yellow]" + messages["salutations"]["thank_you"] + "[/yellow]")

    confirmation = typer.confirm(messages["warnings"]["start_confirmation"])

    if not confirmation:
        mprint("[red]" + messages["warnings"]
               ["program_termination"] + "[/red]" + "[blink][/blink]")

        raise typer.Abort()

    SetupProject.project_setup()


# app run
if __name__ == "__main__":
    myte()
