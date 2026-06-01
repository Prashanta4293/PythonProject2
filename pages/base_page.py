# pages/base_page.py

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.text_content(locator)

    def wait_for_element(self, locator):
        self.page.wait_for_selector(locator)

    def take_screenshot(self, name="screenshot.png"):
        self.page.screenshot(path=f"reports/{name}")