import pytest
from playwright.sync_api import Page, expect

test_data=[('Admin1','admin121','invalid'),
           ('Admi','admin1','invalid'),
           ('Admin','admin123','valid'),
           ('','','invalid')]

@pytest.mark.parametrize("user,pwd,validity",test_data)
def test_verifyLoginPage(user,pwd,validity,page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(pwd)
    page.get_by_role("button",name="Login").click()
    for_fail=page.get_by_text("Invalid credentials")
    for_pass=page.locator("//h6[text()='Dashboard']")
    for_blank= page.locator("//h5[text()='Login']")

    # Validation
    if validity=="valid":
        expect(for_pass).to_be_visible(timeout=10000)
    elif validity=="invalid":
        expect(for_fail).to_be_visible(timeout=10000)
    else:
        expect(for_blank).to_be_visible(timeout=10000)
        expect(page).to_be_visible("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")





