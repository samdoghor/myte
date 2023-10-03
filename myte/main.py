# entry_point.py

"""
This module is the entry point of the application.
All configurations are done here.
"""

import time

import typer
from rich import print as mprint
from tools import CreateProject

# app initialization

myte = typer.Typer()

# application


@myte.command()
def main():
    """ The defines myte main function """

    mprint("""
[yellow]Compatible Note:[/yellow]
Myte requires at least Python 3.11. However, the tool may still work fine
in lower versions not less than 3.8. If you encounter any error, do well to
update your python version. [yellow]Thank you[/yellow]
             """)

    time.sleep(2)

    confirmation = typer.confirm("Do you want to continue?")

    if not confirmation:
        mprint("[red]The programme will now terminate[/red]")

        time.sleep(2)
        raise typer.Abort()

    # Call the create_project function from the CreateProject class
    CreateProject.create_project()

    time.sleep(2)


# app run
if __name__ == "__main__":
    myte()
