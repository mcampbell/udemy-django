from playwright.sync_api import Page, expect


def test_any_month(page: Page):
    for month in ["january", "february"]:
        page.goto(f"http://localhost:8000/challenges/{month}")
        expect(page.locator("css=body")).to_contain_text(f"My goal for {month}.")

