# utils/generic_functions.py

import time

class GenericFunctions:

    @staticmethod
    def wait(seconds=2):
        time.sleep(seconds)

    @staticmethod
    def generate_random_email():
        return f"test{int(time.time())}@mail.com"

    @staticmethod
    def take_screenshot(page, name):
        page.screenshot(path=f"reports/{name}.png")