# Multistage build structure:
#
# python FROM $FROM_IMAGE
# ├── poetry
# └── dev-deps
#     ├── dev (FINAL)
# .   └── qa (FINAL)

ARG FROM_IMAGE
FROM $FROM_IMAGE as python
ARG TARGET_WORKDIR
WORKDIR $TARGET_WORKDIR

FROM python as poetry
ARG POETRY_HOME=/poetry
ADD https://install.python-poetry.org /tmp/poetry-install.py
RUN python3 /tmp/poetry-install.py && \
    ln -s /poetry/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false && \
    poetry config installer.parallel true

FROM python as dev-deps
ENV INVOKE_LOCAL true
COPY --from=poetry /poetry /poetry
COPY README.md poetry.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/pypoetry \
    ln -s /poetry/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false && \
    poetry config installer.parallel true && \
    poetry install --with dev --no-interaction --no-ansi

FROM dev-deps as dev
ARG USER_NAME
ARG USER_UID
RUN useradd \
    --create-home \
    --no-log-init \
    --shell /bin/bash \
    --uid $USER_UID \
    $USER_NAME
# Set site-packages ownership to the user
RUN chown -R $USER_UID:$USER_UID $(python -c "import site; print(site.getsitepackages()[0])")
USER $USER_NAME
RUN poetry config virtualenvs.create false && \
    poetry config installer.parallel true
CMD ["sleep", "infinity"]

FROM dev-deps as qa
COPY . .
CMD ["invoke", "qa"]
