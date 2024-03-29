# constants.py

"""
This module defines constants use for this project
"""

import json
import os
import platform

# get template folder path

# template_folder = os.path.join(os.path.dirname(__file__), "templates")
template_folder = os.path.join(os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)), "templates")


# get current working directory path

current_dir = os.getcwd()

# get messages file

parent_folder = os.path.join(os.path.dirname(__file__))
file_path = os.path.join(parent_folder, 'info.json')
with open(file_path, "r", encoding='utf-8') as f:
    messages = json.load(f)


# get OS

system_os = platform.system()
