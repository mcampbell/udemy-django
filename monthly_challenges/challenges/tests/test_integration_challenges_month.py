from playwright.sync_api import Page, expect


def test_index(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/")
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
        locator = page.get_by_test_id(f"{month.lower()}-challenge")
        expect(locator).to_contain_text(month)


def test_any_month_with_string(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/january")
    expect(page.locator("h1")).to_contain_text("Challenge For January")
    expect(page.locator("#challenge")).to_contain_text("Your challenge for January")
    expect(page).to_have_title("January Challenge")


def test_any_month_with_int(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/1")
    expect(page.locator("h1")).to_contain_text("Challenge For January")
    expect(page.locator("#challenge")).to_contain_text("Your challenge for January")


def test_bad_month(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/Nope")
    expect(page.locator("body")).to_contain_text("Invalid month")


def test_bad_integer_month(page: Page) -> None:
    page.goto("http://localhost:8000/challenges/13")
    expect(page.locator("body")).to_contain_text("Invalid month")
