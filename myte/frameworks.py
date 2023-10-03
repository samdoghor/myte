"""
Ths module lists out all framework available for selection
"""


from rich import print as rprint
import inquirer



def main():
    """ The server : Pyframeboiler """

    rprint("""
[yellow]Welcome, Pyframeboiler helps you setup your python
frameworks easily and faster. Developed by Samuel, Doghor Destiny
(https://samdoghor.com)
Github: https://github.com/samdoghor/pyframeboiler [/yellow]
""")
    choices = ["Option 1", "Option 2", "Option 3"]

    questions = [

        inquirer.List(
            "choice",
            message="Select an option:",
            choices=choices,
            carousel=True,  # Enables arrow key navigation
        )
    ]

    answers = inquirer.prompt(questions)

    typer.echo(f"Selected option: {answers['choice']}")