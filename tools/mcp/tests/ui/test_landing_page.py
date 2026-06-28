"""Landing page UI, style, and navigation regression tests."""

from playwright.sync_api import Page, expect


def test_root_redirects_to_en(page: Page, base_url: str) -> None:
    page.goto(f"{base_url}/")
    expect(page).to_have_url(f"{base_url}/en")


def test_landing_ui_and_styles(page: Page, base_url: str) -> None:
    page.goto(f"{base_url}/en")

    expect(page.get_by_test_id("nav-logo-home")).to_contain_text("PyQuest")
    expect(page.get_by_text("Learn Python like a game")).to_be_visible()
    expect(page.get_by_role("heading", name="Welcome back, Creator!")).to_be_visible()
    expect(
        page.get_by_text("Pick a course and keep your adventure going.")
    ).to_be_visible()

    expect(page.locator("header")).to_have_css("position", "sticky")

    welcome = page.get_by_role("heading", name="Welcome back, Creator!")
    expect(welcome).to_have_css("font-weight", "900")

    card_one = page.get_by_test_id("course-card-course-1")
    card_two = page.get_by_test_id("course-card-course-2")
    expect(card_one).to_contain_text("Python Basics")
    expect(card_two).to_contain_text("Web Apps with Flask")

    cta_pill = card_one.locator("span.bg-violet-500")
    matches_violet_500 = cta_pill.evaluate(
        """(el) => {
            const actual = getComputedStyle(el).backgroundColor;
            const probe = document.createElement("span");
            probe.className = "bg-violet-500";
            probe.style.visibility = "hidden";
            document.body.appendChild(probe);
            const expected = getComputedStyle(probe).backgroundColor;
            document.body.removeChild(probe);
            return actual === expected;
        }"""
    )
    assert matches_violet_500

    expect(page.get_by_test_id("lang-toggle-en")).to_have_attribute(
        "aria-pressed", "true"
    )


def test_course_cards_navigate_to_course_maps(page: Page, base_url: str) -> None:
    page.goto(f"{base_url}/en")

    page.get_by_test_id("course-card-course-1").click()
    expect(page).to_have_url(f"{base_url}/en/course-1")

    page.goto(f"{base_url}/en")
    page.get_by_test_id("course-card-course-2").click()
    expect(page).to_have_url(f"{base_url}/en/course-2")


def test_language_toggle_switches_locale(page: Page, base_url: str) -> None:
    page.goto(f"{base_url}/en")

    page.get_by_test_id("lang-toggle-ru").click()
    expect(page).to_have_url(f"{base_url}/ru")
    expect(
        page.get_by_role("heading", name="С возвращением, Создатель!")
    ).to_be_visible()

    page.get_by_test_id("lang-toggle-en").click()
    expect(page).to_have_url(f"{base_url}/en")


def test_nav_logo_returns_home(page: Page, base_url: str) -> None:
    page.goto(f"{base_url}/en/course-1")
    page.get_by_test_id("nav-logo-home").click()
    expect(page).to_have_url(f"{base_url}/en")
