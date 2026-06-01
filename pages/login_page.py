# pages/login_page.py

from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.login_btn = "button[type='submit']"

    def login(self, user, pwd):
        self.fill(self.username, user)
        self.fill(self.password, pwd)
        self.click(self.login_btn)