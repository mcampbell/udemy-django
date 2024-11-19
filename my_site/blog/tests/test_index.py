from playwright.sync_api import Page, expect


def test_index(page: Page):
    page.goto("http://localhost:8000/blog")
    _common_expectations(page)


def test_root_goes_to_blog(page: Page) -> None:
    page.goto("http://localhost:8000/")
    _common_expectations(page)


def _common_expectations(page: Page) -> None:
    expect(page).to_have_title("Blog Index")
    expect(page.locator("header#main-navigation h1 a")).to_have_text("My Udemy Blog")
    expect(page.locator("section#welcome header h2")).to_have_text("My Blog")
