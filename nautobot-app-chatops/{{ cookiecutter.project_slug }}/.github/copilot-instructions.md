# Copilot Repository Instructions --- Nautobot ChatOps App

You are **GitHub Copilot** working inside a **Nautobot ChatOps App** repository.
Your mission is to generate **small, readable, test-backed** changes that follow
**Nautobot patterns** and **ChatOps-specific patterns** for building interactive
chat commands.

> **Location:** Save this file at `.github/copilot-instructions.md`.  
> **Scope:** You may also add path-scoped rules via
> `.github/instructions/*.instructions.md` if truly necessary.

---

## 0) Quick Facts (for Copilot)

- **Stack:** Django app that runs inside **Nautobot** (network SoT &
  automation). Uses Postgres, Redis, and Celery via Nautobot. Prefer idiomatic
  **Django** and **Nautobot helper APIs**.
- **ChatOps:** This app extends Nautobot ChatOps functionality with **worker
  functions**, **subcommands**, and **dispatcher patterns** for chat platform
  integration (Slack, Microsoft Teams, Webex, Mattermost).
- **Python:** 3.9–3.13 commonly in use.
- **Dependency & venv:** **Poetry** only.
- **Task runner:** `invoke` (always via Poetry).
- **Style:** Ruff + Pylint; **imports at the top**; prefer **docstrings over
  inline comments**; clear, explicit code.

---

## 1) Tooling & Environment (Poetry-first)

Always use Poetry for dependency management and virtualenvs.

- Install deps:  
  `poetry install`
- **Run tasks (required):**  
  `poetry run invoke <task> [args]`

Examples:
- `poetry run invoke autoformat`
- `poetry run invoke ruff`
- `poetry run invoke pylint`
- `poetry run invoke tests`
- `poetry run invoke check-migrations`
- `poetry run invoke makemigrations -n <name>`
- `poetry run invoke markdownlint`
- `poetry run invoke yamllint`

Prefer `invoke` tasks over ad-hoc commands. **When suggesting commands, prefix them
with `poetry run`.**

---

## 2) Style, Lint, and Documentation

- **Ruff** is used for formatting and linting; **Pylint** for static analysis.
  Generated code must pass both.
- **Imports:**  
  - Place **all imports at the top** of the file (after the module docstring).  
  - No wildcard imports; prefer absolute imports and explicit symbols.  
  - Aliasing Nautobot app modules is fine for clarity, e.g.:  
    `from nautobot.ipam import models as ipam_models`
  - Prefer imports from `nautobot.apps` instead of `nautobot.core`
- **Docstrings > inline comments:**  
  - Keep inline comments to the minimum for non-obvious logic.  
  - Put purpose/params/returns/side-effects in **module/class/function
    docstrings**.  
- Write straightforward, readable code over clever one-liners.
- **Docs:**
  - If you add/change features, update `docs/` accordingly.
  - Use `mkdocs` syntax.
  - Run `poetry run invoke markdownlint` to validate and resolve any issues with
    the markdown syntax.
  - Run `poetry run invoke yamllint` to validate YAML files (e.g., mkdocs.yml).
  - Run `poetry run invoke build-and-check-docs` to validate.

---

## 3) Use Nautobot's Frameworks (default choices)

When scaffolding features, use Nautobot's base classes and helpers first:

- **Models:** `PrimaryModel` (full Nautobot features) or `BaseModel` as
  appropriate.
- **Forms:** `NautobotModelForm` (+ `NautobotBulkEditForm` for bulk edits).
- **FilterSets:** `NautobotModelFilterSet` (`Meta.fields = "__all__"` unless
  strongly justified).
- **Serializers:** `NautobotModelSerializer` (writeable) / `BaseModelSerializer`
  (simple read-only).
- **API views:** `NautobotModelViewSet`.
- **UI views:** `NautobotUIViewSet` (unifies list/detail/edit/delete).
- **URLs/Routes:** Use helpers such as `get_route_for_model()`; do **not**
  hand-craft route strings.

**Why:** These reduce boilerplate, align with core Nautobot behavior, and improve
maintainability.

---

## 4) Models & Data Layer

- Prefer natural keys (e.g., unique `name`) or PKs; add `slug` only with clear
  rationale.
- Use constant `CHARFIELD_MAX_LENGTH` for text lengths unless you have a very good
  reason not to.
- Avoid `null=True` on strings; use empty string `""` when semantically empty.
- For `ManyToManyField`, declare an explicit **through** model. We follow the
  convention of using both model names and the word Assignment for **through**
  models. Ex. `AccessPointDeviceAssignment`
- If searchable, populate `searchable_models` on the `NautobotAppConfig` in the
  `__init__.py` file.

---

## 5) Forms, Filters, Templates, and UI Patterns

- **Forms:**  
  - Use `DynamicModelChoiceField` for large foreign keys.  
  - Put complex validation in `clean()` (model or form as appropriate).
- **Filters:**  
  - Use `RelatedMembershipBooleanFilter` for boolean relationship filters
    (`has_*`).  
  - Use `NaturalKeyOrPKMultipleChoiceFilter` for FK filters where applicable.
- **Templates:**  
  - Extend Nautobot base templates; prefer provided filters
    (`|hyperlinked_object`, `|placeholder`, etc.) over `mark_safe`/hand-rolled
    anchors.
- **UI Patterns:**  
  - Prefer **tabs** (via `NautobotUIViewSet`) for distinct data categories.  
  - Use full-width detail layouts for dense content.  
  - Provide **stats tiles** / instance counts if helpful.  
  - For long-running actions, use **AJAX modal + polling** (Jobs/Celery).  
  - Use inline edit sparingly and always re-validate server-side.

---

## 6) Migrations

- If models change:  
  - `poetry run invoke check-migrations`  
  - `poetry run invoke makemigrations -n <meaningful_name>`
- Keep schema and data migrations separate and reversible.
- Use descriptive migration names (e.g., `devicenote_initial`, `provider_increase_account_length`).
- Ruff-format generated migrations for consistency.

---

## 7) Tests --- What to Generate (Nautobot-style, **required**)

**Use Nautobot's testing base classes and mixins. Don't use `unittest.TestCase`
or raw `django.test.TestCase`.**

### 7.1 Test Types & Base Classes

- **Unit tests:** inherit from `nautobot.apps.testing.TestCase` (auto-tagged `unit`).
- **View tests:** use `nautobot.apps.testing.ViewTestCases` mixins.
- **API tests:** use `nautobot.apps.testing.APIViewTestCases` mixins
  (`CreateObjectViewTestCase`, `ListObjectsViewTestCase`, `GetObjectViewTestCase`,
  `UpdateObjectViewTestCase`, `DeleteObjectViewTestCase`, and bulk variants).
  These enforce `?brief=` behavior (declare `brief_fields`) and exercise bulk
  endpoints.
- **Filter tests:** use `nautobot.apps.testing.FilterTestCases` (generic
  boolean/multi-choice/tags tests).
- **Form tests:** use `nautobot.core.testing.FormTestCases.BaseFormTestCase`.
- **Integration (browser) tests:** `nautobot.apps.testing.SeleniumTestCase`
  (auto-tagged `integration`).
- **Migration tests:** `django_test_migrations.MigratorTestCase` (auto-tagged
  `migration_test`).

### 7.2 Directory Layout

```text
<app>/tests/
  test_models.py
  test_filters.py
  test_api.py
  test_views.py
  integration/
    test_*.py
  migration/
    test_*.py
```text

### 7.3 Running Tests

- All tests (fast fixtures enabled):

**Help**

```text
poetry run invoke tests
```text

```text
Usage: inv[oke] [--core-opts] tests [--options] [other tasks here ...]

Docstring:
  Run all tests for this app.

Options:
  -f, --failfast    fail as soon as a single test fails don't run the entire test
                    suite. (default: False)
  -k, --keepdb      Save and re-use test database between test runs for faster
                    re-testing. (default: False)
  -l, --lint-only   Only run linters; unit tests will be excluded. (default: False)
```text

### 7.4 Test Data & Fixtures

- Prefer creating objects via model `.create()`/`.save()` inside tests.
- Avoid calling factories in `setUp()` / `setUpTestData()`; factory output can be
  stateful.
- Rely on cached/seeded fixtures where provided by the runner to keep tests fast
  and deterministic.

### 7.5 API Test Skeleton (what Copilot should scaffold)

```python
"""API tests for Widget."""
from nautobot.apps.testing import APIViewTestCases
from . import models

class WidgetAPITests(
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
):
    """CRUD tests for the Widget REST API."""
    model = models.Widget

    # Returned keys for `?brief=true` (sorted)
    brief_fields = ["display", "id", "name", "url"]

    @classmethod
    def SetUpTestData(cls):
        cls.create_data = [
            {"name": "Widget A"},
            {"name": "Widget B"},
        ]
        cls.update_data = {"name": "Widget A+"}
```text

### 7.6 Filter Test Skeleton

```python
"""Filter tests for Widget."""
from nautobot.apps.testing import FilterTestCases
from . import filters as widget_filters, models

class WidgetFilterTests(FilterTestCases.FilterTestCase):
    """Generic filter assertions for WidgetFilterSet."""
    filterset = widget_filters.WidgetFilterSet
    queryset = models.Widget.objects.all()

    # Optional: map filter names to queryset kwargs to exercise generic cases.
    generic_filter_tests = [
        ["name", "name"],
        # ["owner_id", "owner__id"],
    ]
```text

### 7.7 Views Test Skeleton

```python
"""View tests for Widget UI."""
from nautobot.apps.testing import ViewTestCases
from . import models

class WidgetUIViewTests(ViewTestCases.PrimaryObjectViewTestCase):
    """UI list/detail/create/edit/delete tests for Widget."""
    model = models.Widget
    bulk_edit_data = {"name": "Bulk Renamed"}
```text

### 7.8 OpenAPI Schema Checks

Add a lightweight OpenAPI schema test using Nautobot's provided test cases to
ensure your app's endpoints and serializers remain schema-valid.

### 7.9 Unittest Task (Django/Nautobot runner)

In addition to `invoke tests` (the default Nautobot test runner), this repo can
use **Django's unittest-style runner** via the `unittest` Invoke task when
present. Prefer this when you want stock unittest selection semantics or when a
plugin/app intends to mirror Nautobot core's runner behavior.

**Help**  
```text
poetry run invoke unittest -h
```text
```text
Usage: inv[oke] [--core-opts] unittest [--options] [other tasks here ...]

Docstring:
  Run Nautobot unit tests.

Options:
  -b, --[no-]buffer             Discard output from passing tests
  -c, --coverage                Enable coverage reporting. Defaults to False
  -f, --failfast                Fail fast on first failure
  -k, --keepdb                  Re-use the test database between runs
  -l STRING, --label=STRING     Directory or module label to test (runs subset)
  -p STRING, --pattern=STRING   Select specific test methods/classes/modules
  -s, --skip-docs-build         Skip building docs before tests
  -v, --verbose                 Verbose test output
```text

**When to use which**

- Use `poetry run invoke tests` for the full testing suite experience (ruff,
  yamllint, markdownlint, check_migrations, pylint, build_and_check_docs,
  validate_app_config, unittest, unitttest_coverage, coverage_lcov).
- Use `poetry run invoke **unittest**` for Django/unittest-native selection
  (labels/patterns), quick targeted runs, or parity with Nautobot core's CI
  jobs.

**Common recipes**  
- Run with coverage:  
  `poetry run invoke unittest --coverage`
- Target a specific module (label):  
  `poetry run invoke unittest --label myapp.tests.test_api`
- Match by pattern (method/class):  
  `poetry run invoke unittest --pattern "WidgetAPITests and test_list_objects"`
- Re-use the DB between runs for speed:  
  `poetry run invoke unittest --keepdb`
- Fail fast & suppress noise from passing tests:  
  `poetry run invoke unittest --failfast --buffer`
- Skip docs build if unchanged:  
  `poetry run invoke unittest --skip-docs-build`

> **Note:** Always prefix with `poetry run` to ensure tests execute inside the
project's Poetry environment.

---

## 8) ChatOps-Specific Patterns & Architecture

### 8.1 Worker Functions Structure

ChatOps apps follow a **three-layer architecture**: input (views/sockets) → worker
→ output (dispatchers).

**Worker module organization:**
- Main worker function in `worker.py` using `handle_subcommands()`
- Subcommands using `@subcommand_of()` decorator
- Each subcommand function takes `dispatcher` as first argument

**Main worker skeleton:**
```python
"""Worker functions implementing Nautobot "mycommand" command and subcommands."""

from nautobot_chatops.workers import subcommand_of, handle_subcommands

def mycommand(subcommand, **kwargs):
    """Interact with mycommand app."""
    return handle_subcommands("mycommand", subcommand, **kwargs)

@subcommand_of("mycommand")
def get_device_info(dispatcher, device_name):
    """Get device information from Nautobot."""
    # Worker logic here
    return True  # or False, or (status, details)
```text

### 8.2 Subcommand Patterns

**Function naming:** Use underscores; they convert to hyphens in chat
(`get_device_info` → `get-device-info`)

**Required signature:** `def subcommand_func(dispatcher, arg1, arg2=None, ...):`

**Return values:**
- `return False` - Command incomplete (prompting user), don't log
- `return True` - Command succeeded
- `return CommandStatusChoices.STATUS_SUCCEEDED` - Command succeeded
  (explicit)
- `return (CommandStatusChoices.STATUS_FAILED, "Error details")` - Command
  failed with details

**Multi-word arguments:** Support quoted arguments by preserving quotes in prompts:
```python
action = f"get-sites location '{city}'"  # Preserve quotes for multi-word params
dispatcher.prompt_for_text(action_id=action, help_text="Enter number", label="Limit")
```text

### 8.3 Dispatcher Interface Patterns

**Platform-agnostic output:** Workers call dispatcher methods; never
platform-specific APIs directly.

**Common dispatcher methods:**
- `dispatcher.send_markdown(text)` - Simple markdown message
- `dispatcher.send_blocks(blocks)` - Rich formatted blocks
- `dispatcher.send_large_table(headers, *rows)` - Table data
- `dispatcher.prompt_from_menu(action, text, choices)` - Interactive menu
- `dispatcher.prompt_for_text(action_id, help_text, label)` - Text input prompt
- `dispatcher.command_response_header(command, subcommand)` - Standard header blocks

**Block formatting example:**
```python
dispatcher.send_blocks([
    *dispatcher.command_response_header("mycommand", "get-device"),
    dispatcher.markdown_block(f"Device: **{device.name}**"),
    dispatcher.markdown_block(f"Status: {device.status}"),
])
```text

### 8.4 Parameter Validation & User Prompting

**Progressive prompting:** If required parameters missing, prompt user and return
`False`:
```python
@subcommand_of("mycommand")
def get_device_info(dispatcher, site_name=None, device_name=None):
    """Get device information."""
    if not site_name:
        sites = [
            (site.name, site.slug) for site in Location.objects.filter(location_type__name="Site")
        ]
        dispatcher.prompt_from_menu("mycommand get-device-info", "Select site", sites)
        return False
  
    if not device_name:
        devices = Device.objects.filter(location__slug=site_name)
        choices = [(dev.name, dev.name) for dev in devices]
        dispatcher.prompt_from_menu(
            f"mycommand get-device-info {site_name}", "Select device", choices
        )
        return False
  
    # Process the command
    device = Device.objects.get(name=device_name)
    dispatcher.send_markdown(f"Device **{device.name}** status: {device.status}")
    return True
```text

### 8.5 Platform Considerations & Output Formatting

**Text limits:** Different platforms have different limits:
- Slack: ~4000 characters for messages, ~3000 for blocks
- Microsoft Teams: ~69 character line wrapping, no preformatted text in cards

**Responsive design:**
- Use `send_large_table()` for data that might exceed platform limits
- Use `send_blocks()` for rich formatting when possible
- Fall back to `send_markdown()` for simple text

**Table handling:**
```python
# For large datasets that may exceed platform limits
dispatcher.send_large_table(
    ["Device", "Site", "Status", "IP Address"],
    *[(dev.name, dev.location.name, dev.status, dev.primary_ip) for dev in devices]
)
```text

### 8.6 Error Handling & Status Reporting

**Graceful error handling:**
```python
@subcommand_of("mycommand")
def risky_operation(dispatcher, device_name):
    """Perform operation that might fail."""
    try:
        device = Device.objects.get(name=device_name)
        # Perform operation
        dispatcher.send_markdown(f"✅ Operation completed for {device.name}")
        return True
    except Device.DoesNotExist:
        dispatcher.send_markdown(f"❌ Device '{device_name}' not found")
        return (CommandStatusChoices.STATUS_FAILED, f"Device {device_name} not found")
    except Exception as exc:
        dispatcher.send_markdown(f"❌ Operation failed: {exc}")
        return (CommandStatusChoices.STATUS_FAILED, str(exc))
```text

### 8.7 Testing ChatOps Commands

**Test structure for workers:**
```python
"""Tests for mycommand ChatOps workers."""
from unittest.mock import Mock, patch
from nautobot.apps.testing import TestCase
from nautobot_chatops.tests.helpers import ChatOpsTestCase
from . import worker

class MyCommandWorkerTest(ChatOpsTestCase):
    """Test mycommand worker functions."""
  
    def test_get_device_info_success(self):
        """Test successful device info retrieval."""
        mock_dispatcher = Mock()
        device = self.device_factory()
  
        result = worker.get_device_info(mock_dispatcher, device.name)
  
        self.assertTrue(result)
        mock_dispatcher.send_markdown.assert_called_once()
  
    def test_get_device_info_missing_params(self):
        """Test prompting when parameters missing."""
        mock_dispatcher = Mock()
  
        result = worker.get_device_info(mock_dispatcher)
  
        self.assertFalse(result)
        mock_dispatcher.prompt_from_menu.assert_called_once()
```text

---

## 9) Celery & Jobs

- For long-running work or external calls, prefer **Celery tasks** or **Nautobot
  Jobs**.
- Do **not** block web requests with heavy processing.
- **ChatOps workers run in Celery:** All ChatOps commands execute as Celery
  tasks, so they can handle longer operations without blocking the chat platform
  response.

---

## 10) Security & Secrets

- Never hard-code secrets/tokens/credentials.  
- Use Nautobot Secrets / External Integrations.  
- Scrub PII and sensitive network details from examples/tests.
- **ChatOps security:** Commands inherit Nautobot user permissions; ensure
  proper user account linking between chat platforms and Nautobot accounts.

---

## 11) Performance & DB

- Prefer queryset filters/bulk ops over per-row loops.  
- Use `select_related` / `prefetch_related` where appropriate.  
- Add indexes for frequently filtered fields; justify in migration message.

---

## 12) Git & Branching

- Small, focused branches.  
- PRs must include tests, migration notes (if any), and "how to test" steps.  
- Reference related issues.  
- Target the repository's active development branch (not `main` if `main` is
  reserved for releases).

---

## 13) PR Hygiene --- What Copilot Should Suggest

- Clear, action-oriented title and description.  
- Link to issue(s) and include screenshots/GIFs for UI work.  
- Call out any migrations and potential data impacts.  
- Keep the diff small and logically cohesive.

---

## 14) Snippets Copilot Should Prefer

**ChatOps Worker Function**
```python
"""Worker functions implementing Nautobot "mycommand" command and subcommands."""
from nautobot_chatops.workers import subcommand_of, handle_subcommands
from nautobot.dcim.models import Device

def mycommand(subcommand, **kwargs):
    """Interact with mycommand app."""
    return handle_subcommands("mycommand", subcommand, **kwargs)

@subcommand_of("mycommand")
def get_device_status(dispatcher, device_name=None):
    """Get the status of a device."""
    if not device_name:
        devices = Device.objects.all()[:20]  # Limit choices
        choices = [(dev.name, dev.name) for dev in devices]
        dispatcher.prompt_from_menu(
            "mycommand get-device-status", "Select device", choices
        )
        return False
  
    try:
        device = Device.objects.get(name=device_name)
        dispatcher.send_blocks([
            *dispatcher.command_response_header("mycommand", "get-device-status"),
            dispatcher.markdown_block(f"**Device:** {device.name}"),
            dispatcher.markdown_block(f"**Status:** {device.status}"),
            dispatcher.markdown_block(f"**Location:** {device.location}"),
        ])
        return True
    except Device.DoesNotExist:
        dispatcher.send_markdown(f"❌ Device '{device_name}' not found")
        return False
```text

**ChatOps Worker Test**
```python
"""Tests for mycommand ChatOps workers."""
from unittest.mock import Mock
from nautobot.apps.testing import TestCase
from nautobot.dcim.models import Device
from . import worker

class MyCommandWorkerTest(TestCase):
    """Test mycommand worker functions."""
  
    def test_get_device_status_success(self):
        """Test successful device status retrieval."""
        mock_dispatcher = Mock()
        device = Device.objects.create(
            name="test-device", device_type=self.device_type, location=self.location
        )
  
        result = worker.get_device_status(mock_dispatcher, device.name)
  
        self.assertTrue(result)
        mock_dispatcher.send_blocks.assert_called_once()
  
    def test_get_device_status_prompts_when_no_device(self):
        """Test prompting when no device specified."""
        mock_dispatcher = Mock()
  
        result = worker.get_device_status(mock_dispatcher)
  
        self.assertFalse(result)
        mock_dispatcher.prompt_from_menu.assert_called_once()
```text

**Model**
```python
"""DeviceNote model."""
from django.db import models
from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
from nautobot.apps.models.generics import PrimaryModel

class DeviceNote(PrimaryModel):
    """Freeform note attached to a device."""
    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH, unique=True)
    content = models.TextField(blank=True, default="")
    tenant = models.ForeignKey(
        to="tenancy.Tenant",
        on_delete=models.PROTECT,
        related_name="device_notes",
        blank=True,
        null=True,
    )
  
    class Meta:
        ordering = ("name",)

    def __str__(self):
        """Stringify instance."""
        return self.name
```text

**Serializer**
```python
"""Serializer for DeviceNote."""
from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin
from .models import DeviceNote

class DeviceNoteSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):
    """Serialize DeviceNote objects."""
    class Meta:
        model = DeviceNote
        fields = "__all__"
```text

**FilterSet**
```python
"""FilterSet for DeviceNote."""
from nautobot.apps.filters import NautobotFilterSet, TenancyModelFilterSetMixin
from .models import DeviceNote

class DeviceNoteFilter(TenancyModelFilterSetMixin, NautobotFilterSet):
    """Filter DeviceNote by name/content."""
    class Meta:
        model = DeviceNote
        fields = "__all__"
```text

**API ViewSet**
```python
"""API viewset for DeviceNote."""
from nautobot.apps.api import NautobotModelViewSet
from .filters import DeviceNoteFilter
from .serializers import DeviceNoteSerializer
from .models import DeviceNote

class DeviceNoteViewSet(NautobotModelViewSet):
    """List, retrieve, and manage DeviceNotes via REST API."""
    queryset = DeviceNote.objects.all()
    serializer_class = DeviceNoteSerializer
    filterset_class = DeviceNoteFilter
```text

**UI ViewSet**
```python
"""UI viewset for DeviceNote."""
from nautobot.apps.views import NautobotUIViewSet
from .models import DeviceNote
from .tables import DeviceNoteTable
from .forms import DeviceNoteForm

class DeviceNoteUIViewSet(NautobotUIViewSet):
    """UI for listing, viewing, creating, and editing DeviceNotes."""
    queryset = DeviceNote.objects.all()
    table = DeviceNoteTable
    bulk_update_form_class = DeviceNoteForm
    form_class = DeviceNoteForm
```text

**Migrations (command)**
```text
poetry run invoke makemigrations -n devicenote_initial
```text

---

## 15) Optional: Folder-Specific Instructions

If needed, add `.github/instructions/*.instructions.md` with path-scoped
front-matter to apply specialized guidance to certain subtrees (e.g., `docs/`,
`nautobot_plugin_tooling/`). Keep rules minimal to avoid confusion.

---

## 16) Final Checklist (for every change)

- [ ] Commands are shown as `poetry run invoke ...`  
- [ ] Imports are at the top; docstrings explain intent/usage  
- [ ] Nautobot base classes, viewsets, and helpers are used  
- [ ] **ChatOps workers use `@subcommand_of()` decorator and proper dispatcher
      interface**
- [ ] **ChatOps functions return appropriate status (True/False/status tuple)**
- [ ] **ChatOps commands handle missing parameters with progressive prompting**
- [ ] Tests cover models/filters/API/views **and ChatOps workers** with Nautobot
      base classes & mixins  
- [ ] Migrations are checked/generated, named meaningfully, and reversible  
- [ ] Querysets are optimized; indexes added if needed  
- [ ] No secrets/PII in code, tests, or docs  
- [ ] Pre-commit hooks pass; Ruff & Pylint clean  
- [ ] PR description includes "how to test" and references related issues

---

## 17) Authoritative Nautobot Repositories & Examples

When proposing or generating **Nautobot-specific code**, prefer patterns proven in
the official repositories below.
Use them for import paths, base-class usage, testing mixins, viewset patterns,
job/celery conventions, and UI Component Framework examples.

- **Nautobot Core:** https://github.com/nautobot/nautobot/
- **Nautobot App --- ChatOps:**
  https://github.com/nautobot/nautobot-app-chatops
- **Nautobot App --- SSoT:** https://github.com/nautobot/nautobot-app-ssot
- **Nautobot App --- Nornir:** https://github.com/nautobot/nautobot-app-nornir
- **Nautobot App --- Golden Config:** https://github.com/nautobot/nautobot-app-golden-config
- **Nautobot App --- DNS Models:** https://github.com/nautobot/nautobot-app-dns-models
- **Nautobot App --- Firewall Models:** https://github.com/nautobot/nautobot-app-firewall-models
- **Nautobot App --- BGP Models:**
  https://github.com/nautobot/nautobot-app-bgp-models

**Guidance for Copilot**
- Prefer examples from these repos over generic Django code.
- Mirror **base class** usage (`PrimaryModel`, `NautobotModelViewSet`,
  `NautobotUIViewSet`, etc.).
- Follow **testing** patterns under `nautobot/apps/testing` (mixins and tags)
  rather than ad-hoc tests.
- **For ChatOps patterns:** Study `nautobot-app-chatops` workers, dispatchers,
  and command structure.
- Reuse **filter/serializer** patterns and import paths exactly as shown in the
  official code.
- Avoid v1-only patterns; target **Nautobot 2.x** APIs and UI Component
  Framework.
- If proposing URLs, prefer helper utilities (e.g., `get_route_for_model`) visible
  in Nautobot core, not hard-coded strings.
