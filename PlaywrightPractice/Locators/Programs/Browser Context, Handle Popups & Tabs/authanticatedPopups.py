#https://the-internet.herokuapp.com/basic_auth
from playwright.sync_api import Page, expect, Playwright
import pytest

# First approach not recommended
def test_authpopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()

# Second approach recommended
def test_secauthpopup(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(
        http_credentials={"username":"admin","password":"admin"}
    )
    page=context.new_page()

    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_timeout(3000)




