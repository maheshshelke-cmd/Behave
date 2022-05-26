from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select




class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check(self):
        pass

