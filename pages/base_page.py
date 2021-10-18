from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os
import pytest


class Base:

    @pytest.fixture()
    def set_up(self):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        PATH = os.path.join(PROJECT_ROOT, "../driver/chromedriver")
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.seleniumframework.com/Practiceform/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
