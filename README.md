# IDS706 Assignment 1

[![Python tests](https://github.com/luel-du/IDS706-Assignment-1/actions/workflows/test.yml/badge.svg)](https://github.com/luel-du/IDS706-Assignment-1/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/python-3.12-blue)

## About

A small Python project for the IDS706 Data Engineering course that demonstrates a complete development workflow: working code with automated tests, a Dockerfile with `.dockerignore` for containerized runs, a Makefile for setup/testing/linting, and GitHub Actions CI that runs tests and lint checks on every push. The app itself asks for a name and prints a welcome message.

## Project structure

```
IDS706-Assignment-1/
├── .github/
│   └── workflows/
│       └── test.yml        # CI: lint + tests
├── src/
│   └── main.py             # Application code
├── tests/
│   └── test_main.py        # Automated tests
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Mac / Linux
.venv\Scripts\activate         # Windows
make install
```

## Usage

Run the app and enter your name when prompted:

```bash
make run
```

```
Enter your name: Luel
Luel, welcome to the Data Engineering course.
```

## Makefile commands

| Command             | Description                                      |
|---------------------|--------------------------------------------------|
| `make install`      | Install dependencies                             |
| `make lint`         | Lint the code with ruff                          |
| `make format`       | Auto-format the code with ruff                   |
| `make format-check` | Verify formatting without changing files         |
| `make test`         | Run the test suite with pytest                   |
| `make check`        | Run lint, format check, and tests together       |
| `make run`          | Run the application                              |
| `make docker-build` | Build the Docker image                           |
| `make docker-run`   | Run the application inside Docker                |
| `make docker-test`  | Run the test suite inside Docker                 |
| `make clean`        | Remove caches and generated files                |

## Docker

```bash
make docker-build
make docker-run
```

## CI/CD

GitHub Actions ([test.yml](.github/workflows/test.yml)) runs on every push and pull request:

- **Lint job**: `ruff` lint and formatting checks
- **Test job**: pytest locally, then builds the Docker image and runs the tests inside the container
