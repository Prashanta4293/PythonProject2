from playwright.sync_api import Page, expect

def test_single_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

# 3 ways to select option from dropdown
#     page.locator('#country').select_option("India") #Select by label
#     page.locator('#country').select_option(label="India") #Select by label

    # page.locator("#country").select_option("india") #select by value
    # page.locator("#country").select_option(value="india")  # select by value

    page.locator("#country").select_option(index=6) #select by index
    page.wait_for_timeout(2000)

    # count option
    option_count= page.locator("#country>option")
    print("Total dropdown option count:",option_count.count())
    expect(option_count).to_have_count(10)




