from playwright.sync_api import Page, expect

def test_verify_radbtn(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Visibility of the element and enable or not
    male_radio= page.locator("#male")
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    expect(male_radio).not_to_be_checked()

    # male_radio.click()
    male_radio.check()   #we can use any one of the click/check function
    page.wait_for_timeout(3000)

    expect(male_radio).to_be_checked()







