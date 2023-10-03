"""
This module is entry point of the application.
All configurations are done here
"""

# imports

import sys


import typer
from rich import print as mprint


# app initialisation

myte = typer.Typer()


# application

@myte.command()
def main():
    """ The defines myte main function """

    mprint("""
[red] Compactible Note: [/red]
[yellow] Myte requires Python 3.10+. However, some templates require a lower
version to work, please upgrade if prompted.
             """)


# app run
if __name__ == "__main__":
    myte()
