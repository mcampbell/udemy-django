from playwright.sync_api import Page, expect


def test_no_month_given(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/")
    locator = page.locator("body")
    for month in [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]:
        expect(locator).to_contain_text(month)


def test_any_month_with_string(page: Page) -> None:
    for month in ["january", "february"]:
        page.goto(f"http://localhost:8000/challenges/{month}")
        expect(page.locator("body")).to_contain_text(
            f"Your challenge for {month.title()}"
        )


def test_bad_month(page: Page) -> None:
    page.goto(f"http://localhost:8000/challenges/Nope")
    expect(page.locator("body")).to_contain_text(f"Invalid month")


def test_any_month_with_int(page: Page) -> None:
    page.goto(f"http://localhost:8000/challenges/1")
    expect(page.locator("body")).to_contain_text(f"Your challenge for January")

    page.goto(f"http://localhost:8000/challenges/3")
    expect(page.locator("body")).to_contain_text(f"Your challenge for March")

    page.goto(f"http://localhost:8000/challenges/13")
    expect(page.locator("body")).to_contain_text(f"Invalid month")
