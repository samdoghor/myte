# create_project.py

"""
This module defines the functions that create the boilerplate.
"""

import os
import shutil

from constants import current_dir, template_folder, messages, system_os
from rich import print as mprint


class CreateProject:
    """ This class defines the boilerplate creation """

    @staticmethod
    def create_dir(project_name, selected_framework, selected_setup):
        """ This function defines the creation of directory """

        source_folder = os.path.join(template_folder,
                                        f"template-{selected_framework['framework'].lower()}-{selected_setup['setup'].lower()}")  # noqa
        destination_folder = os.path.join(current_dir, project_name)

        shutil.copytree(source_folder, destination_folder)

        mprint("[blue]" + messages["success"]["project_success"] + "[/blue]")
        mprint("[yellow]Usage:[/yellow]")
        mprint("[green]Run the commands below:[/green]")
        mprint(
            f"""[magenta] {messages["usage_message"]["cd_message"]}{project_name} [/magenta]""")  # noqa

        if system_os in ("Linux", "Darwin"):
            if system_os == "Darwin":
                mprint(messages["os"]["macOS"])

            if system_os == "Linux":
                mprint(messages["os"]["linux"])

            mprint(messages["usage_message"]
                   ["virtualenv_install_message_linux_mac"])
            mprint(messages["usage_message"]
                   ["create_virtualenv_message_linux_mac"])
            mprint(messages["usage_message"]
                   ["activate_virtualenv_message_linux_mac"])

        if system_os == "Windows":
            mprint(messages["os"]["windows"])
            mprint(messages["usage_message"]
                   ["virtualenv_install_message_windows"])
            mprint(messages["usage_message"]
                   ["create_virtualenv_message_windows"])
            mprint(messages["usage_message"]
                   ["activate_virtualenv_message_windows"])

        mprint(messages["usage_message"]["install_requirements_message"])

    @staticmethod
    def create_files(selected_framework, selected_setup):
        """ This function defines the creation of directory """

        source_folder = os.path.join(template_folder,
                                        f"template-{selected_framework['framework'].lower()}-{selected_setup['setup'].lower()}")  # noqa

        destination_folder = current_dir

        for file in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            if os.path.isfile(source_path):
                shutil.copy(source_path, destination_path)
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)

        # shutil.copytree(source_folder, destination_folder)

        mprint("[blue]" + messages["success"]["project_success"] + "[/blue]")
        mprint("[yellow]Usage:[/yellow]")
        mprint("[green]Run the commands below:[/green]")

        if system_os in ("Linux", "Darwin"):
            if system_os == "Darwin":
                mprint(messages["os"]["macOS"])

            if system_os == "Linux":
                mprint(messages["os"]["linux"])

            mprint(messages["usage_message"]
                   ["virtualenv_install_message_linux_mac"])
            mprint(messages["usage_message"]
                   ["create_virtualenv_message_linux_mac"])
            mprint(messages["usage_message"]
                   ["activate_virtualenv_message_linux_mac"])

        if system_os == "Windows":
            mprint(messages["os"]["windows"])
            mprint(messages["usage_message"]
                   ["virtualenv_install_message_windows"])
            mprint(messages["usage_message"]
                   ["create_virtualenv_message_windows"])
            mprint(messages["usage_message"]
                   ["activate_virtualenv_message_windows"])

        mprint(messages["usage_message"]["install_requirements_message"])
