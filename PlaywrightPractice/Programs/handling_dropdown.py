import pytest
from playwright.sync_api import Page, expect

# def test_single_select_dropdown(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#
# # 3 ways to select option from dropdown
# #     page.locator('#country').select_option("India") #Select by label
# #     page.locator('#country').select_option(label="India") #Select by label
#
#     # page.locator("#country").select_option("india") #select by value
#     # page.locator("#country").select_option(value="india")  # select by value
#
#     page.locator("#country").select_option(index=6) #select by index
#     page.wait_for_timeout(2000)
#
#     # count option
#     option_count= page.locator("#country>option")
#     print("Total dropdown option count:",option_count.count())
#     expect(option_count).to_have_count(10)

def test_multi_select_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

# 3 ways to multiselect option from dropdown
#     page.locator("#colors").select_option(["Red", "Green", "Blue"]) #select by label
#     page.locator("#colors").select_option(label=["Red", "Green", "Yellow"])  # select by label
#     page.wait_for_timeout(2000)

#     page.locator("#colors").select_option(["red","blue","white"]) #Select by value
#     page.locator("#colors").select_option(value=["red", "white", "green"]) #Select by value
#     page.wait_for_timeout(2000)

    # page.locator("#colors").select_option(index=[0,2,4]) #Select by index
    # page.wait_for_timeout(2000)
    dropdown_options= page.locator("#colors>option")
    # dropdown_options= page.locator("#animals>option")

    options_text=[text.strip() for text in dropdown_options.all_text_contents()]

    original_list=options_text.copy()
    sorted_list=sorted(original_list)

    if original_list==sorted_list:
        print("Dropdown options in sorted order")
        assert True #pytest function
    else:
        print("Dropdown list is not in sorted order")
        assert False






