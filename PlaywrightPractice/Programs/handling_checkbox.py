from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Select specific checkbox
    sunday_checkbox= page.get_by_label("Sunday")
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

    # checked all the checkbox in one shot and verify is enabled or not
    # for day in days:
    #     checkbox= page.get_by_label(day)
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()
    #     page.wait_for_timeout(1000)

#     OR
    checkboxes= [page.get_by_label(day) for day in days]
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
        page.wait_for_timeout(1000)

    # Uncheck the last 3
    for checkbox in checkboxes[-1:-9:-2]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
        page.wait_for_timeout(1000)

    # Toggle checkbox
    for checkbox in checkboxes:
        if checkbox.is_checked():
            checkbox.uncheck()
            page.wait_for_timeout(1000)
        else:
            checkbox.check()
            page.wait_for_timeout(1000)

    # Random checkbox selected- 1,3,6
    indexes= [1,3,5]

    for i in indexes:
        checkboxes[i].check()
        page.wait_for_timeout(1000)

    # Verify checkbox by label
    week = "Sunday"

    for i in days:
        if i==week:
            page.get_by_label(week).uncheck()
            page.wait_for_timeout(1000)











