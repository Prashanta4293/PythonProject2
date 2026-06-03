from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Select specific checkbox
    sunday_checkbox= page.get_by_label("SUnday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    # count number of check boxes
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxes= []

    # for day in days:
    #     checkbox= page.get_by_label(day)
    #     checkboxes.append(checkbox)
    #OR
    checkboxes= [page.get_by_label(day) for day in days] #List comprehension

    print("Total number of checkboxes:", len(checkboxes))




