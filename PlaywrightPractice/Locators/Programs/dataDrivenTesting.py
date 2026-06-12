import pytest
from playwright.sync_api import Page, expect

search_items= ['laptop', 'computer', 'Gift card']

@pytest.mark.parametrize("items",search_items)
def test_readExcel(items,page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(items)
    page.locator("//input[@type='submit']").click()
    page.wait_for_timeout(2000)
    first_result= page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(items,ignore_case=True)






