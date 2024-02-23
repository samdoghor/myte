# Myte ✨

> Python web framework boilerplate made easy

![GitHub Release](https://img.shields.io/github/v/release/samdoghor/myte) ![GitHub License](https://img.shields.io/github/license/samdoghor/myte)

Myte allows users to choose from popular web frameworks like Flask, FastAPI, and Tornado when initializing a new project. After entering a project name, the user selects their preferred framework which then generates the basic directory structure and boilerplate code to get started. **The project is still at it early phase alot of expected features are be missing**.

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

Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/)

```Bash Copy
pip install myte
```

or

```Bach Copy
python3 -m pip install myte
```

## Usage

Install `Myte` once without a virtual environment so it would be available to bootstrap all your web projects.

### How to start your web project in any of the frameworks

- Create a virtual environment
- Activate the virtual environment
- Run the code below

```Bash Copy
create-myte
```

### How it looks without an activated virtual environment

```Bash Copy
$ create-myte

Compatible Note:
Myte requires at least Python 3.8. However, the tool may still work
fine in lower versions. If you encounter any error, do well to report
them here https://cutt.ly/1wSR7LW0
Thank you


Do you want to continue? [y/N]: y

Project Name (myte-project):


 ✅ Project name: myte-project


[?] Select a framework: Flask
 > Flask
   Flask-Restful-API

 ✅ Flask,  selected


[?] Select a framework: Simple
 > Simple
   Robust

 ✅ Simple,  selected


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

```

### How it looks with an activated virtual environment

```Bash Copy
$ create-myte

Compatible Note:
Myte requires at least Python 3.8. However, the tool may still work
fine in lower versions. If you encounter any error, do well to report
them here https://cutt.ly/1wSR7LW0
Thank you


Do you want to continue? [y/N]: y

Project Name (myte-project):


 ✅ Project name: myte-project


[?] Select a framework: Flask
 > Flask
   Flask-Restful-API

 ✅ Flask,  selected


[?] Select a framework: Simple
 > Simple
   Robust

 ✅ Simple,  selected


Project setup complete


Usage:
Run the commands below:
 - cd myte-project
 -> Your OS is Windows
 - pip install -r requirements.txt
 - Rename example.env to .env
 - Go to config.py, decide the database you want to use, uncomment it
and run the pip instructions there
 - Go to .env, replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' in SECRETKEY with -> og3dOuRYNcnItH2XbYHMYHffbMcBxsS0

```

## Contribution

See [Contributing Guide](CONTRIBUTING.md).

## License

[MIT](LICENSE).
