from challenges.views import FEB_OUTPUT, JAN_OUTPUT
from playwright.sync_api import Page


def test_jan(page: Page):
    page.goto("http://localhost:8000/challenges/january")
    assert page.content().count(JAN_OUTPUT) > 0


def test_feb(page: Page):
    page.goto("http://localhost:8000/challenges/february")
    assert page.content().count(FEB_OUTPUT) > 0
