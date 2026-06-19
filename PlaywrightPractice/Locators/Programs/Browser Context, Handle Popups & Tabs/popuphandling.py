from playwright.sync_api import Page, expect, Playwright
import pytest

def test_popup_handle(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()

    page1.goto("https://testautomationpractice.blogspot.com/")

    #  Not Recommended
    # def handle_popup(popup):
    #     popup.wait_for_load_state()
    # page1.on("popup",handle_popup)

    # OR

    # Recommended using lambda function
    # page1.on("popup",lambda popup:popup.wait_for_load_state())

    page1.locator("#PopUp").click()
    page1.wait_for_timeout(3000)

    all_popup=context.pages
    print("Total numbers of popups/pages:",len(all_popup))

    # For extract the pages urls
    for pw in all_popup:
        print(pw.url)
        title=pw.title()
        print(title)
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(3000)
            pw.close() #Cloced only playwright window
        if "Selenium" in title:
            pw.locator(".navbar-toggler-icon").click()
            pw.wait_for_timeout(3000)
            pw.close() #closed only Selenium window









