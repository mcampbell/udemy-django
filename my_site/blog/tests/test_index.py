from playwright.sync_api import Page, expect


def test_index(page: Page):
    page.goto("http://localhost:8000/blog")
    _common_expectations(page)


def test_root_goes_to_blog(page: Page) -> None:
    page.goto("http://localhost:8000/")
    _common_expectations(page)


def _common_expectations(page: Page) -> None:
    expect(page.locator("text=Welcome to my site!")).to_be_visible()
    expect(page).to_have_title("Blog Index")
