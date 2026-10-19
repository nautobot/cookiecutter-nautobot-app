# Running the Playwright Tests

Browser tests for this app are in `{{ cookiecutter.app_name }}/tests/integration/`. They are pytest
tests and drive a real browser against a running Nautobot. They are separate from the unittest
suite, which still runs with `invoke unittest`.

!!! note
    Write each test directly, like the ones already in `{{ cookiecutter.app_name }}/tests/integration/`.
    Do not add base classes or shared helpers for other apps to reuse. How app browser tests
    should be shared between repositories has not been decided yet.

The process running pytest imports `nautobot.playwright`, which was added in Nautobot 3.3. The
instance under test does not need it. The suite, `--look` and scratch tests run against the
default development stack at `nautobot_ver`. The `playwright` image installs its own Nautobot
for the client. `playwright_nautobot_ver` in `invoke.yml` sets that version. It is `next` until
3.3 is released, and it does not have to match `nautobot_ver`.

## Test against another Nautobot version

Set the stack's version in `invoke.yml`, then run `invoke build` and `invoke start`:

```yaml
---
{{ cookiecutter.app_name }}:
  nautobot_ver: "next"
```

## Run

`invoke playwright` reads the `local` setting in `invoke.yml` to decide where to run, the same
as every other task.

**In the container (default).** With `local` false the tests run in the `playwright` compose
service, built from `development/Dockerfile-playwright`. It has the browsers, Nautobot and
this app, and reaches the development stack at `http://nautobot:8080`. You do not need to install
anything on the host. Use this path also on a host that Playwright does not support, such as Alpine.

```bash
invoke start
invoke playwright                              # the whole suite
invoke playwright --marker behavioral          # only the behavioral tests
invoke playwright --pattern installed          # only tests matching a name
invoke playwright --url https://nautobot.example.com
```

`invoke playwright` builds the `playwright` image only when no image with its tag exists. The tag
is made from `playwright_nautobot_ver` and the locked pytest and Playwright versions, so
changing any of those builds a new image on the next run. Editing `Dockerfile-playwright` does
not change the tag, so run `invoke build --playwright` after an edit. Because `next` changes
over time, picking up a newer `next` needs `invoke build --playwright --no-cache`. Without it,
Docker reuses the cached layer that installed an older `next`, even one cached by another app
built from the same Dockerfile.

**On the host.** With `local` true pytest runs on your machine. Headed mode, the Playwright
inspector and codegen only work here.

```bash
poetry install --with playwright
poetry run pip install "nautobot @ git+https://github.com/nautobot/nautobot.git@next"
poetry run playwright install chromium
invoke playwright --headed
```

The second line is the host equivalent of `playwright_nautobot_ver`, needed until 3.3 is
released. `poetry.lock` pins the app's own Nautobot, which has no `nautobot.playwright` before
3.3, so without it pytest fails at import before collecting a test. It replaces Nautobot in the
virtualenv only and changes no file in the repository. A later `poetry install` puts the locked
version back.

By default the host run expects `http://localhost:8080`, which is where the development stack
publishes Nautobot. Either way the tests log in as `admin`/`admin` and use the development API
token. Override any of that with `--url`, `--username`, `--password` and `--token`, or with the
matching `NAUTOBOT_PLAYWRIGHT_*` environment variables.

When a test fails, its trace and screenshot are written to `test-results/`, which is gitignored
and cleared at the start of every pytest session. Open a trace with
`poetry run playwright show-trace test-results/<path>/trace.zip`.

On Linux the container writes `screenshots/`, `test-results/` and `.pytest_cache/` as root.
Rootless Docker or Podman is the fix for that; Docker Desktop maps ownership on its own.

Whichever instance you point at has to accept the `Host` header the browser sends. A Nautobot
started with a narrow `ALLOWED_HOSTS` answers `400 Bad Request` to every request.

## Look at one page

`invoke playwright --look <path>` opens one page as `admin` and prints a report instead of
running the suite: the status, title and headings, console errors and warnings, failed or 4xx/5xx
requests, the visible text, and the path of a full-page screenshot under `screenshots/`. It is
for checking a page by eye, or for Claude to read, and runs wherever `invoke playwright` runs.
It only logs in and reads, so it needs no API token and is safe against a shared instance.

```bash
invoke playwright --look /apps/installed-apps/
invoke playwright --look /dcim/devices/ --url http://host.docker.internal:8080
```

Set `NAUTOBOT_PLAYWRIGHT_LOOK_CHARS` to change how much text is printed (default 4000).
`screenshots/` is gitignored and is not cleared between runs, unlike `test-results/`; running
`--look` on the same path again overwrites the earlier screenshot.

**With Claude Code.** Ask in plain words: "does the installed apps page list this app", "take a
screenshot of /dcim/devices/", "write a test for the list view filters". The `testing-nautobot-ui`
skill in `.claude/skills/` loads on its own when a request is about the UI or the browser tests.
It runs `--look` for the first two and follows this guide for the third. There is no slash command.

For anything the report does not cover, write a short test that uses the same fixtures and put
it in `{{ cookiecutter.app_name }}/tests/scratch/`. Everything in that directory is gitignored and
outside the suite, and `invoke playwright --scratch` runs it with print output on. Add
`--pattern` to pick one test. The `testing-nautobot-ui` Claude skill describes both paths.

## In CI

`.github/workflows/playwright.yml` builds the development image at the Nautobot version in its
matrix and the `playwright` image at `playwright_nautobot_ver`, starts Nautobot with
`invoke start --service nautobot`, and runs `invoke playwright`. The suite creates the records it
needs over the REST API. Traces, screenshots and the Nautobot log are uploaded when a test fails.

## Before you write a helper, check what already exists

Nautobot ships the fixtures and page objects these tests are built on. Logging in, generating
unique names, creating and deleting records over the REST API, reading a table, and opening the
filter drawer are all provided.

List every available fixture, with what it does and the file it comes from:

```bash
poetry run pytest --fixtures {{ cookiecutter.app_name }}/tests/integration
```

Page-object methods have no equivalent listing, so read the source:

- `nautobot/playwright/list_page.py` covers list views: row counts, column values, and the whole
  filter drawer.
- `nautobot/playwright/base_page.py` covers navigation, waiting for a page to settle, and URL
  assertions.

If any other app would want the same thing, it belongs in Nautobot rather than here. Add a fixture
to this app only when it is about this app's models, such as a `created_<model>` fixture in
`tests/integration/conftest.py` that builds the records a filter test needs on top of the shared
`create_object` fixture.

## Further reading

Nautobot's own guide to writing these tests covers the page objects, the fixtures, and when to
assert with `expect` rather than `assert`. It is
[playwright-testing.md](https://github.com/nautobot/nautobot/blob/next/nautobot/docs/development/core/playwright-testing.md)
on Nautobot's `next` branch.
