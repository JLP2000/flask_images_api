# Image Sharing API

A simple image sharing api built with Flask also serving html pages on the root domain. Website allows for viewing and creating images, as well as an experimental email subscription service.

## Installation and Usage

### Installation

- Clone or download the repo.

### Usage

- Navigate to folder.
- Run `pipenv shell` to start environment.
- Run `pipenv install`.
- Run `pipenv run dev` to start development server.
- Run `pipenv run test` to start `pytest` testing suite.

## Technologies

- Python
- Flask
- pytest
- flask-mail
- flask-wtf
- werkzeug

## Process

- VSCode Live Share, Josh on api development, Liam on testing development.
- Pair programming on further api and front-end development.

## Challenges and Wins

### Challenges

#### JSON file import

Problems encountered trying to import JSON data from a `.json` file.

**Solution**: Temporarily hard-coded data directly into `images.py`. This will definitely be revisited in order to achieve separation of concerns.

#### Submitting form data for email subscription

`Method not allowed` errors kept appearing after redirection, however managed to solve this by specifying `POST` method on the route decorator.

### Wins

Home page dynamically renders email form or success text based on user interaction.

## Future Features

## Contributors

@JLP2000 :man_technologist:
@liambrockpy :man_technologist:
