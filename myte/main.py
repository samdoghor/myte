# main.py

"""
This module is the entry point of the application.
All configurations are done here.
"""

import typer
from rich import print as mprint
from setup_project import SetupProject

# cli initialization

myte = typer.Typer()

# cli start point


@myte.command()
def main():
    """ The defines myte main function """

    mprint("""
[yellow]Compatible Note:[/yellow]
Myte requires at least Python 3.11. However, the tool may still work fine
in lower versions not less than 3.8. If you encounter any error, do well to
update your python version. [yellow]Thank you[/yellow]
             """)

    confirmation = typer.confirm("Do you want to continue?")

    if not confirmation:
        mprint("[red]The programme will now terminate[/red] [blink][/blink]")

        raise typer.Abort()

    SetupProject.project_setup()


# app run
if __name__ == "__main__":
    myte()
