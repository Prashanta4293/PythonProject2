
from playwright.sync_api import Page, expect


def test_verifyPageURL(page:Page): # page is a fixture
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # Open URL
    myURL= page.url #to get URL
    print("URL is:", myURL)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # Validate URL

def test_verifyPageTitle(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000) # increase timeout
    myTitle= page.title()
    print("Title is:", myTitle)
    expect(page).to_have_title("OrangeHRM")


