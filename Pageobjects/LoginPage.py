from selenium.webdriver.common.by import By

from Pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    loginPage_textfield_email = (By.ID, "Email")
    loginPage_textfield_password = (By.ID, "Password")
    loginPage_button_login = (By.XPATH, "//*[@class='button-1 login-button']")

    def get_Email(self):
        return self.driver.find_element(*LoginPage.loginPage_textfield_email)

    def get_Password(self):
        return self.driver.find_element(*LoginPage.loginPage_textfield_password)

    def get_LoginButton(self):
        return self.driver.find_element(*LoginPage.loginPage_button_login)
