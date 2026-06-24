import re
from playwright.sync_api import Page, expect


def test_Verify_pwBuiltinLocator(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",timeout=60000)

# 1) get_by_alt_text()
    logo= page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()
    print("Verified image")

# 2) get_by_text()
    full_text= page.get_by_text("Username : Admin") #full text
    partial_text= page.get_by_text("Username : ") #partial text
    reg_expression= page.get_by_text(re.compile(r"Username\s*:\s*Admin")) #reg expression
    expect(full_text).to_be_visible()
    expect(partial_text).to_be_visible()
    expect(reg_expression).to_be_visible()
    print("Verified text")
    page.wait_for_timeout(3000)

# 3) get_by_role()
    expect(page.get_by_role("heading",name="Login")).to_be_visible()
    print("Verified header")
    page.wait_for_timeout(3000)

# 4) get_by_placeholder()
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(3000)

# # 5) get_by_label()
#     page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
#     page.get_by_label("Email Address:").fill("prashantkumarbehera1@gmail.com")
#     page.get_by_label("Password:").fill("Test")
#     page.wait_for_timeout(3000)
#
# # 6) get_by_title()
#     expect(page.get_by_title("Home page link")).to_have_text("Home")
#     expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
#
# 7) get_by_test_id()
#     expect(page.get_by_test_id("nav-home")).to_have_text("Home")






