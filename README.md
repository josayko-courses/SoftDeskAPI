# SoftDeskAPI

## Description

A simple API for issue tracking system applications.

## Installation

### Prerequisites

- `python` >= 3.9, `pip`, `pipenv`
- If `python` < 3.9, manage different `python` versions with **[pyenv](https://github.com/pyenv/pyenv)**

### Get started

```bash
$ pipenv install
```

```bash
$ pipenv shell
```

## Running the app

```bash
$ python manage.py runserver
# The API is running on http://localhost:8000/ by default
```

- There are already 3 registered users in the app:
  - id: `1`, user: `admin@admin.org`, password: `admin` (superuser),
  - id: `2`, user: `johndoe@softdesk.org`, password: `testuser`,
  - id: `3`, user: `janesmith@softdesk.org`, password: `testuser`,

## Author

- Jonny Saykosy <josayko@pm.me>

## License & copyright

© Jonny Saykosy

Licensed under the [MIT License](LICENSE).
