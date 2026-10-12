"""One-page report for `invoke playwright --look <path>`: what the page returned, logged, and looks like.

Not part of the suite: it sits outside pytest's `testpaths`, so only the invoke task's explicit
path reaches it. It logs in as the configured user and reads. No API token, no writes to the
instance. The report is printed, so the task runs pytest with `-s`.
"""

import os
import re
from pathlib import Path

TEXT_LIMIT = int(os.environ.get("NAUTOBOT_PLAYWRIGHT_LOOK_CHARS", "4000"))
# Responses at or above this status are listed as problems.
ERROR_STATUS = 400


def test_look(auth_page, base_url):
    """Open the path, then print status, title, headings, console and request problems, text, and a screenshot path."""
    path = os.environ["NAUTOBOT_PLAYWRIGHT_LOOK"]
    console = []
    problems = []
    auth_page.on(
        "console",
        lambda message: (
            console.append(f"{message.type}: {message.text}") if message.type in ("error", "warning") else None
        ),
    )
    auth_page.on(
        "requestfailed", lambda request: problems.append(f"failed {request.method} {request.url}: {request.failure}")
    )
    auth_page.on(
        "response",
        lambda response: (
            problems.append(f"{response.status} {response.request.method} {response.url}")
            if response.status >= ERROR_STATUS
            else None
        ),
    )

    response = auth_page.goto(f"{base_url}{path}")
    auth_page.wait_for_load_state("networkidle")

    slug = re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-") or "root"
    # screenshots/ is ours and persists; pytest clears test-results/ every session.
    screenshot = Path("screenshots") / f"look-{slug}.png"
    screenshot.parent.mkdir(exist_ok=True)
    auth_page.screenshot(path=str(screenshot), full_page=True)

    headings = auth_page.locator("h1, h2, h3").all_inner_texts()
    # The main region when the page has one, so the navigation does not use up the text budget.
    main = auth_page.locator("main, #main, [role=main]")
    text = (main.first if main.count() else auth_page.locator("body")).inner_text()
    truncated = len(text) > TEXT_LIMIT

    print()
    print(f"URL: {auth_page.url}")
    print(f"Status: {response.status if response else 'no response'}")
    print(f"Title: {auth_page.title()}")
    print("Headings: " + (" | ".join(heading.strip() for heading in headings if heading.strip()) or "none"))
    print("Console errors and warnings: " + (f"{len(console)}" if console else "none"))
    for line in console:
        print(f"  {line}")
    print("Failed or 4xx/5xx requests: " + (f"{len(problems)}" if problems else "none"))
    for line in problems:
        print(f"  {line}")
    print(f"Screenshot: {screenshot}")
    print(f"Visible text{' (first ' + str(TEXT_LIMIT) + ' characters)' if truncated else ''}:")
    print(text[:TEXT_LIMIT])

    assert response is not None, f"No response for {path}"
