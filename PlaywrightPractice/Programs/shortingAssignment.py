from playwright.sync_api import Page, expect
#Assignment
#go to bstackdemo.com
#check order by filter dropdown is visible or not/enable or not
#selct lowest to highest option
#print all the title and price of the project in two different list
#print the lowest and highest priced product



def test_assignment(page:Page):
    page.goto("https://bstackdemo.com/")

    orderby_dropdown=page.locator("//div[@class='sort']//select")
    expect(orderby_dropdown).to_be_visible()
    expect(orderby_dropdown).to_be_enabled()
    page.wait_for_timeout(3000)
    orderby_dropdown.select_option(value='lowestprice')
    title= page.locator("//p[@class='shelf-item__title']")
    alltitles=[t for t in title.all_text_contents()]
    # print(alltitles)
    price= page.locator("//div[@class='shelf-item__price']")
    allprices=[p for p in price.all_text_contents()]
    # print(allprices)

    for item, price in zip(alltitles,allprices):
        print(item,":", price)

    #or
    # item_prices=dict(zip(alltitles,allprices))
    # print(item_prices)




