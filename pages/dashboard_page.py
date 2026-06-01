# pages/dashboard_page.py

from pages.base_page import BasePage

class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.dashboard_text = "text=Dashboard"

    def is_dashboard_visible(self):
        self.wait_for_element(self.dashboard_text)
        return True