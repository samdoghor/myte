# Myte Documentation

Python web framework boilerplate made easy (`Start your projects in seconds`)

![Last commit](https://img.shields.io/github/last-commit/samdoghor/myte) ![GitHub Release](https://img.shields.io/github/v/release/samdoghor/myte) ![GitHub License](https://img.shields.io/github/license/samdoghor/myte) ![PyPI - Version](https://img.shields.io/pypi/v/myte?style=plastic) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/myte)

Myte allows users to choose from popular web frameworks like Flask, FastAPI, and Tornado when initializing a new project. After entering a project name, the user selects their preferred framework which then generates the basic directory structure and boilerplate code to get started.

!!! info

    The project is still at it early phase, alot of expected features are missing.

## Why you should use Myte

Choose Myte for effortless web development setup. With intuitive project initialization, pick your preferred framework like Flask or anticipate upcoming options like FastAPI. Whether you're a seasoned developer or just starting out, Myte's user-friendly interface guides you smoothly through setup. Customize project structures to fit your needs with adaptable templates. Stay ahead of the curve with ongoing updates and enhancements, making your web development journey seamless and exciting.

## Features

- 🚀 Project Bootstrapping
- 💡 Simplified project setup
- 🛠️ Framework flexibility
- 📝 Customizable templates
- 💻 Cross-OS functionality

## Supported frameworks

| Framework | Status |
| --------------- | --------------- |
| [Flask](https://flask.palletsprojects.com/) | ✅ Completed |
| [FastAPI](https://fastapi.tiangolo.com/) | 🛠️ Undergoing Development |
| [Tornado](https://www.tornadoweb.org/en/stable/) | ❌ Not started |
| [Bottle](https://bottlepy.org/) | ❌ Not started  |
| [Pyramid](https://trypyramid.com/) | ❌ Not started  |
| [CherryPy](https://docs.cherrypy.dev/en/latest/) | ❌ Not started  |

## Installing

!!! info

    It is `recommended` to Install `Myte` without a virtual environment so it would be available to bootstrap all your web projects going forward.

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)

    pip install myte

or

    python3 -m pip install myte

## Usage

Run the code below to get started

    create-myte

### How it looks after 4 simple steps

!!! note "Step 1"

    `$ create-myte`

    !!! tip 
    
        Enter the value `y` to proceed or `N` to terminate the program

    !!! info ""

        Compatible Note:
        Myte requires at least Python 3.8. However, the tool may still work
        fine in lower versions. If you encounter any error, do well to report
        them here <https://cutt.ly/1wSR7LW0>
        Thank you

        Do you want to continue? [y/N]: `y`

!!! note "Step 2"

    !!! tip 

        Enter your `desired project name` or simply enter `.` (this will erase everything in the current folder) to use current folder.

    !!! info ""

        Project Name (myte-project):

        ✅ Project name: myte-project

!!! note "Step 3"

    !!! tip 

        Use the `up` and `down` `arrow key` to select from the available framework and hit `enter`.

    !!! info ""
        [?] Select a framework: Flask
        > Flask
        Flask-Restful-API

        ✅ Flask,  selected

!!! note "Step 4"

    !!! tip 

        Use the `up` and `down` `arrow key` to select from the available complexity and hit `enter`.

    !!! info ""
        [?] Select complexity: Simple
        > Simple
        Robust

        ✅ Simple,  selected

        !!! success

            Project setup complete

        Usage:
        Run the commands below:

        - cd myte-project
        -> Your OS is Windows
        - pip install virtualenv (if not installed)
        - virtualenv env
        - source env/scripts/activate
        - pip install -r requirements.txt
        - Rename example.env to .env
        - Go to config.py, decide the database you want to use, uncomment it
        and run the pip instructions there
        - Go to .env, replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' in SECRETKEY with -> og3dOuRYNcnItH2XbYHMYHffbMcBxsS0

## Contribution

See [Contributing Guide](https://github.com/samdoghor/myte/blob/main/CONTRIBUTING.md).

## License

[MIT](https://github.com/samdoghor/myte/blob/main/LICENSE).
