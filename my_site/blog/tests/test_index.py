from playwright.sync_api import Page, expect


def test_index(page: Page):
    page.goto("http://localhost:8000/blog")
    expect(page.locator("text=Welcome to the blog!")).to_be_visible()

def test_root_goes_to_blog(page:Page) -> None:
    page.goto("http://localhost:8000/")
    expect(page.locator("text=Welcome to the blog!")).to_be_visible()
