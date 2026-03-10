ARG PYTHON_VER
FROM python:$PYTHON_VER

# Add poetry install location to the $PATH
ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

WORKDIR /source

COPY README.md poetry.lock pyproject.toml ./
RUN poetry install
