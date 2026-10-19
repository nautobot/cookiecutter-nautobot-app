{%- set model_const = cookiecutter.model_class_name | camel_case_to_kebab | replace("-", "_") | upper -%}
{#- Sorted at bake time: ruff's import order depends on where the model name falls against PACKAGE_NAME. -#}
{%- set imported_names = ["PACKAGE_NAME", "VERBOSE_NAME"] -%}
{%- if cookiecutter.model_class_name != "None" -%}
{%- set imported_names = imported_names + [model_const ~ "_LIST_HEADING", model_const ~ "_LIST_PATH"] -%}
{%- endif -%}
"""The app is installed{% if cookiecutter.model_class_name != "None" %} and its list page is reachable{% endif %}.

Any app can reuse this test. It uses no page object and no table markup, only the values in
`constants.py`.
"""

from playwright.sync_api import expect

from {{ cookiecutter.app_name }}.tests.integration.constants import (
{%- for name in imported_names | sort %}
    {{ name }},
{%- endfor %}
)


class AppRegistrationTestCase:
    """The app registers with Nautobot{% if cookiecutter.model_class_name != "None" %} and serves its list page{% endif %}."""

    def test_app_is_installed(self, api):
        """Nautobot reports the app among its installed apps."""
        response = api.get("/api/apps/installed-apps/")
        assert response.ok, f"GET /api/apps/installed-apps/ returned {response.status}: {response.text()}"
        packages = [app["package"] for app in response.json()]
        assert PACKAGE_NAME in packages, f"{PACKAGE_NAME} missing from installed apps: {packages}"

    def test_installed_apps_page_lists_app(self, auth_page, base_url):
        """The Installed Apps page shows the app by name."""
        auth_page.goto(f"{base_url}/apps/installed-apps/")
        expect(auth_page.locator("table tbody").get_by_text(VERBOSE_NAME, exact=True).first).to_be_visible()
{%- if cookiecutter.model_class_name != "None" %}

    def test_list_page_loads(self, auth_page, base_url):
        """The list page renders its heading and table, and the sidebar links to it.

        The table rows load in a second request after the page frame. If that request fails, the
        table body stays empty, while an empty list still renders one "no records" row. A visible
        first row therefore shows that the second request succeeded.
        The link count is scoped to the sidebar tabs because the Favorites flyout adds a
        second, hidden link for any starred page.
        """
        list_path = {{ model_const }}_LIST_PATH
        auth_page.goto(f"{base_url}{list_path}")
        expect(auth_page.get_by_role("heading", name={{ model_const }}_LIST_HEADING).first).to_be_visible()
        expect(auth_page.locator("table tbody tr").first).to_be_visible()
        expect(auth_page.locator(f"nav#sidenav li[data-section-name] a[href='{list_path}']")).to_have_count(1)
{%- endif %}
