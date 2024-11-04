from playwright.sync_api import Page, expect

from challenges.views import FEB_OUTPUT, JAN_OUTPUT


def test_jan(page: Page):
    page.goto("http://localhost:8000/challenges/january")
    expect(page.locator("css=body")).to_contain_text(JAN_OUTPUT)


def test_feb(page: Page):
    page.goto("http://localhost:8000/challenges/february")
    expect(page.locator("css=body")).to_contain_text(FEB_OUTPUT)
