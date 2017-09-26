# Reel Picker

A friendly application to help you choose what to watch tonight. Stop searching and get watching.

This is an academic project. Its purpose is to experiment with new technologies, increase our skills with known ones and share the knowledge. Things will sometimes be overexplained; this is normal.

## Requirements

To have this project up and running, you first need some basic stuff.

### On Windows

- [Download Python along with Pip](https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe).
- Add both your python directory and its `Scripts` subdirectory to your Path.
- Install [Virtualenv](https://virtualenv.pypa.io/en/stable/) from the command prompt (`pip install virtualenv`).
- Install [Virtualenvwrapper for Windows](https://github.com/davidmarble/virtualenvwrapper-win/) from the command prompt (`pip install virtualenvwrapper-win`).


### On POSIX (MacOS, Linux, etc)

- [Download Python along with Pip](https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe).
- ... _(Add to Path, to be clarified)_
- Install [Virtualenv](https://virtualenv.pypa.io/en/stable/) from the command prompt (`pip install virtualenv`).
- Install [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) from the command prompt (`pip install virtualenvwrapper`).

## API Setup and Activation

### On Windows

#### Initial Setup

1. Navigate to the `API` directory with your favorite command prompt.
2. Enter `mkvirtualenv -a . -r requirements.txt reel-picker-api`. This will activate the virtual environment.
3. You may deactivate the virtual environment you juste created by typing `deactivate`.

#### Working on the API

1. Make sure you're up to date (`git pull`).
2. Type in `workon reel-picker-api` from the `API` folder to activate the virtual environment.
3. Type in `pip install -r requirements.txt` to install new requirements.
4. Do what you want (change code, test the api, add requirements).
5. If you added new requirements, type in `pip freeze > requirements.txt` and commit/push your changes.
6. Use the `deactivate` command when you're done.

### App Setup

1. ...

## Running a local server

1. ...

## Building the App

1. ...
