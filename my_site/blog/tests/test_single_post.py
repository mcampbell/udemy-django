from playwright.sync_api import Page, expect


def test_all_posts(page: Page):
    page.goto("http://localhost:8000/blog/posts/some_slug")
    expect(page.locator("text=Post with slug: some_slug")).to_be_visible()
