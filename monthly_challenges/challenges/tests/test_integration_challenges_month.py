from playwright.sync_api import Page, expect


def test_any_month_with_string(page: Page):
    for month in ["january", "february"]:
        page.goto(f"http://localhost:8000/challenges/{month}")
        expect(page.locator("body")).to_contain_text(f"My goal for {month}.")


def test_any_month_with_int(page: Page):
    for month in range(2):
        page.goto(f"http://localhost:8000/challenges/{month}")
        expect(page.locator("body")).to_contain_text(f"My goal for the month number {month}.")
