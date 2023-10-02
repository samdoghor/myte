"""
This module is entry point of the application.
All configurations are done here
"""

import time
# pylint: disable=E0401
import typer
# pylint: disable=E0401

# pylint: disable=W0622
from rich import print
# pylint: disable=W0622
from commands import select_framework


# app initialisation

server = typer.Typer()

frameworks = ["Django", "Flask", "Express.js",
              "Ruby on Rails", "Spring Boot", "Laravel"]


@server.command()
def main():
    """ The server : Pyframeboiler """
    print("""
          [bold green]Welcome[/bold green],

          Pyframeboiler helps you setup your webframework
          easily and faster.
          """)

    time.sleep(3)

    select_framework()


# server run


if __name__ == "__main__":
    server()
