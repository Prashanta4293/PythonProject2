import pytest
from playwright.sync_api import Page, expect, Playwright


def test_browserContext(playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page1= context.new_page()

    page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")