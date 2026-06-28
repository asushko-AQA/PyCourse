from playwright.sync_api import Page, expect


class AppShellPage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def goto(self, path: str) -> None:
        self.page.goto(f"{self.base_url}{path}")

    def goto_home(self, lang: str = "en") -> None:
        self.goto(f"/{lang}")

    def click_logo_home(self) -> None:
        self.page.get_by_test_id("nav-logo-home").click()

    def switch_language(self, lang: str) -> None:
        self.page.get_by_test_id(f"lang-toggle-{lang}").click()

    def expect_url_path(self, path: str) -> None:
        expect(self.page).to_have_url(f"{self.base_url}{path}")
