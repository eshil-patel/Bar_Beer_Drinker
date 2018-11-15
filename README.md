# BarBeerDrinker Demo Project

This project is structured so that there are two folders - one for UI development using Angular and the other for the server-side application using Flask.

## Running a development version of the UI

To run the UI, go to the bar-beer-drinker-ui folder and first make sure you have the dependencies installed.
To do this, you need to have Node.js and NPM (comes with Node.js) installed and then execute:

```
npm install
```

This will get all the dependencies based on the package.json file.

Afterwards, you will also need to have Angular CLI installed on a global level.

```
npm install -g @angular/cli
```

To run the UI code, use:

```
ng serve
```

To build a final distribution package of the UI code:

```
ng build
```

This will create a `dist` folder containing all the files that need to be included into your server-side application folder under the static folder (go to Flask documentation for further details on this).

## Running the Flask application locally

To run the Flask application locally, make sure you first have the virtual environment setup.

Install `virtualenv`
```
pip install virtualenv
```

Activate the virtual environment
```
./venv/Scripts/activate.bat
```

or

```
./venv/bin/activate
```

### Installing Python project dependencies

Make sure you have the virtual environment activated - there should be `(venv)` next to the bash prompt in the terminal.

```
pip install -r requirements.txt
```

### Running the application in development

To run the application
```
python app.py
```
