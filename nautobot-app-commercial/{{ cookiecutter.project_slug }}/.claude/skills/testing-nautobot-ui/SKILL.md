---
name: testing-nautobot-ui
description: Use when you need to look at a page of the Nautobot web UI in this repo's dev environment (check it renders, read what is on it, take a screenshot, find console or request errors), or to add or run a Playwright browser test. Both run through `invoke playwright`, in the `playwright` compose service or on the host.
---

# Looking at and testing the Nautobot UI with Playwright

This skill covers two tasks. Looking at a page needs no code. Writing a test uses the framework in `{{ cookiecutter.app_name }}/tests/integration/`.

## Look at a page

```bash
invoke playwright --look /dcim/devices/
```

The command prints a report of that page, logged in as `admin`: status, title, headings, console errors and warnings, failed or 4xx/5xx requests, the visible text (first 4000 characters; raise `NAUTOBOT_PLAYWRIGHT_LOOK_CHARS` for more), and the path of a full-page screenshot under `screenshots/`. It only logs in and reads the page. It needs no API token and changes nothing on the instance, so it is also safe against a shared or public Nautobot (`--url`, `--username`, `--password`). Open the screenshot and look at it. `screenshots/` is gitignored and persists across runs; running `--look` on the same path again overwrites the earlier screenshot. This is the first thing to reach for when asked whether a page renders, what it shows, or why it looks wrong. "Take a screenshot of /dcim/devices/" is the same command; show the screenshot and skip the rest of the report.

If the page must be clicked into or changed before the screenshot, use a scratch test (below) instead.

## Screenshot or inspect a page in a specific state

`--look` only opens a URL. When the page must be in some state first (a button clicked, a tab open, a form filled, a modal showing), or the report does not answer the question (for example, you need to read one element), write a short scratch test that gets the page into that state and then takes the screenshot. Put it in `{{ cookiecutter.app_name }}/tests/scratch/`, which is gitignored and outside the suite, so it never sits next to the shipped tests and never runs with them. All the framework fixtures are available there: a logged-in page (`auth_page`), the instance URL (`base_url`), a REST client (`api`) and record cleanup (`create_object`). The debug toolbar is already off. Only `api` and `create_object` need a token; a test that just reads the page runs against any instance with a login.

```python
from playwright.sync_api import expect


def test_scratch_device_tab(auth_page, base_url):
    # Without a UUID, open the list and click the link in the first row.
    auth_page.goto(f"{base_url}/dcim/devices/")
    first_link = auth_page.locator("table tbody tr a").first
    expect(first_link).to_be_visible()
    first_link.click()

    auth_page.get_by_role("tab", name="Interfaces").click()
    expect(auth_page.locator("table tbody tr").first).to_be_visible()

    auth_page.screenshot(path="screenshots/scratch-device-tab.png", full_page=True)
    # Or just one element: auth_page.get_by_role("dialog").screenshot(path=...)
    print(auth_page.url)
```

The selectors above are examples; take the real ones from a `--look` run of the page. With a UUID, go straight there: `auth_page.goto(f"{base_url}/dcim/devices/{uuid}/")`. To find one by name, use `api.get("/api/dcim/devices/", params={"name": "..."}).json()["results"][0]["id"]` (needs a token).

Run it with `invoke playwright --scratch --pattern device_tab` (`--pattern` is pytest `-k`; print output is on for scratch runs), then open the PNG and look at it. If a step fails, the run still leaves a failure screenshot under `test-results/`; read that to see how far it got, before the next run clears it. Do not write standalone Playwright scripts, and do not put files in a temporary directory outside the repository. Run everything through `invoke playwright`, and save screenshots under `screenshots/`.

### Another user, or no login

Every page starts from the session login: `admin`, or whatever `--username` and `--password` set for the whole run. For one test as a different user, or with no login at all, override the context args on the test. The test still gets `base_url` and the header that turns off the debug toolbar; only the saved login is removed.

```python
import pytest
from nautobot.playwright.helpers import log_in


@pytest.mark.browser_context_args(storage_state=None)
def test_scratch_as_other_user(page):
    log_in(page, "someuser", "somepassword")  # drop this line for a logged-out page
    page.goto("/dcim/devices/")
```

For several users in one test, request the `new_context` fixture instead of `page`, call it once per user, and log each page in. Set `storage_state` with the marker, not as an argument. `new_context(storage_state=None)` raises `TypeError`, because pytest-playwright calls `browser.new_context(**browser_context_args, **kwargs)`, so `storage_state` arrives twice. The user must already exist on the instance. Nautobot core has no fixture yet that creates a user with chosen permissions; one is planned as follow-up work.

## Write a browser test

Browser tests are pytest tests built on the fixtures and page objects Nautobot ships in `nautobot.playwright` (3.3 or later). The developer guide is `docs/dev/playwright.md`; read it before writing a test. Tests live in `{{ cookiecutter.app_name }}/tests/integration/`. Page objects go in a `pages/` module in that directory, and shared fixtures go in a `conftest.py` there. Use `expect` for anything on the page, `assert` for Python values, and `expect(...).not_to_*` for negative checks.

`invoke playwright` runs the suite. Like every other task, it reads `local` in `invoke.yml` to decide where to run:

- `local` false (default): pytest runs in the `playwright` compose service, which has the
  browsers, Nautobot and this app, and reaches the development stack at `http://nautobot:8080`.
- `local` true: pytest runs on the host. The host needs `poetry install --with playwright` and
  `poetry run playwright install chromium`. Headed mode works only here.

```bash
invoke playwright                              # whole suite
invoke playwright --pattern create             # tests whose name contains "create"
invoke playwright --marker behavioral          # one pytest mark
invoke playwright --url http://host.docker.internal:8080   # a Nautobot on the host machine
```

## Gotchas

- **The instance does not need Nautobot 3.3.** The default development stack works. Only the process running pytest needs `nautobot.playwright` (3.3 or later). The `playwright` image installs it from `playwright_nautobot_ver` in `invoke.yml`, `next` by default.
- **Rebuilding the playwright image** needs `invoke build --playwright`. Plain `invoke build` skips it, and `invoke playwright` builds it only when its tag is missing.
- **The dev stack must be running** (`invoke start`). Ask the user to start it, or for a `--url` to another instance, rather than starting it yourself, because `invoke start` builds images. The `playwright` service itself does not need to be up: `invoke playwright` starts a one-off container when it is not.
- After `page.goto(...)`, wait for the element you will read or screenshot, for example
  `expect(page.locator("table tbody tr").first).to_be_visible()`. List rows arrive through htmx after the page frame. When there is no single element to wait for, for example before a full-page screenshot, call `BasePage(page, base_url).wait_for_load()` from `nautobot.playwright.base_page`. Do not use `wait_for_load_state("networkidle")`. A page that polls, such as an unfinished job result, never reaches it, and the test fails at the timeout.
- Never hardcode the host or port. Build URLs from `base_url`.
- In a full-page screenshot the left sidebar ends partway down. It is fixed to the window, and full-page capture cuts fixed elements. This is not a layout bug. Against the public demo site, the Aha feedback and LinkedIn requests fail on every page. The fixtures add a header that turns off the debug toolbar to every request, and those third-party servers reject it under CORS. The app is not the cause.
- `test-results/` contains only failure traces and screenshots, and pytest clears it at the start of every session. `screenshots/` is where `--look` and scratch tests write, and it is kept. Both are gitignored. On Linux a container run writes them as root.
