from playwright.sync_api import Page, expect


def test_verify_checkbox_radiobtn(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Visibility of the element and enable or not
    name= page.locator("input#name")
    expect(name).to_be_visible()
    expect(name).to_be_enabled()

def test_to_check_the_attribute_of_the_element(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    name = page.locator("input#name")
    expect(name).to_have_attribute("maxlength","15")

    # get an attribute value of an element
    maxlength= name.get_attribute("maxlength")
    print(maxlength)

    # Fill the text
    name.fill("Prashanta Behera")
    page.wait_for_timeout(2000)

    # get the input value from input box
    entered= name.input_value()
    print("Input value is:", entered)






