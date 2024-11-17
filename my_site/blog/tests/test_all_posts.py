from playwright.sync_api import Page, expect

def test_all_posts(page: Page):
    page.goto("http://localhost:8000/blog/posts")
    expect(page.locator("text=List of posts")).to_be_visible()
