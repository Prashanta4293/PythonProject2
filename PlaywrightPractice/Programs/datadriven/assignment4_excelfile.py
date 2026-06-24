import pytest
from playwright.sync_api import Page, expect
import openpyxl #pip install openpyxl

test_data= [] #empty list

# Read excel file
workbook=openpyxl.load_workbook("PlaywrightPractice/Locators/Programs/testdata/data.xlsx")
sheet=workbook.active  # or worksheet["Sheetname"]

# Reading data from excel using for loop
for row in sheet.iter_rows(min_row=2, values_only=True):
    user, pwd, validity = row
    test_data.append(((str(user) or ""),(str(pwd) or ""),(str(validity) or "")))
workbook.close()

@pytest.mark.parametrize("user,pwd,validity",test_data)
def test_verifyLoginPage_csv(user,pwd,validity,page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(pwd)
    page.get_by_role("button",name="Login").click()
    for_fail=page.get_by_text("Invalid credentials")
    for_pass=page.locator("//h6[text()='Dashboard']")
    for_blank= page.locator("//h5[text()='Login']")

    # Validation
    if validity=="valid":
        expect(for_pass).to_be_visible(timeout=15000)
    elif validity=="invalid":
        expect(for_fail).to_be_visible(timeout=15000)
    else:
        expect(for_blank).to_be_visible(timeout=15000)
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

