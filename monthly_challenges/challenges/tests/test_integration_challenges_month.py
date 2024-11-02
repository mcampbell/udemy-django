from playwright.sync_api import Page


def test_has_text(page: Page):
    page.goto("http://localhost:8000/challenges/january")

    assert page.content().count("This works!") > 0
