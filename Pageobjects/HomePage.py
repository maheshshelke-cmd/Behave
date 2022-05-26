import time

from selenium.webdriver.common.by import By

from Pageobjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Homepage_link_customerMenu = (By.XPATH, "//*[@class='mt-2']/ul/li[4]")
    Homepage_link_customerSubMenu = (By.XPATH, "//*[@class='mt-2']/ul/li[4]//ul//li[1]/a")
    Homepage_link_AddNew = (By.XPATH, "//*[@class='content-header clearfix']/div/a")

    def get_CustomerMenu(self):
        return self.driver.find_element(*HomePage.Homepage_link_customerMenu)

    def get_CustomerSubMenu(self):
        return self.driver.find_element(*HomePage.Homepage_link_customerSubMenu)

    def get_AddNew(self):
        return self.driver.find_element(*HomePage.Homepage_link_AddNew)





