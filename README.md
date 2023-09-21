# Cookiecutter Templates for Creating Nautobot Apps

## Local Quickstart

For local usage or development.

Pre-requisites:

- Docker and Docker Compose
- git
- Python 3.8+ with pip

Install dependencies:

```shell
pip install invoke python-dotenv toml
```

Clone the repository:

```shell
git clone git@github.com:nautobot/cookiecutter-nautobot-app.git
cd cookiecutter-nautobot-app
```

Run all tests:

```shell
invoke tests
```

List all available tasks

```shell
invoke help
```
