from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class Reusable_functions:

    def __init__(self,driver):
        self.driver = driver

    def openBrowser(self, URL):
        self.driver.get(URL)

        self.driver.implicitly_wait(5)

    def type(self, webElement, Value):
        webElement.clear()
        webElement.send_keys(Value)

    def click(self,webElement):
        webElement.click()

    def getText(self, webElement):
        text = webElement.text()
        return text

    def getTitle(self):
        title = self.driver.title
        return title

    def selectByValue(self,webElement,value):
        dropdown = Select(webElement)
        dropdown.select_by_value(value)

    def selectByIndex(self,webElement,value):
        dropdown = Select(webElement)
        dropdown.select_by_index(value)

    def selectByVisibleText(self,webElement,value):
        dropdown = Select(webElement)
        dropdown.select_by_visible_text(value)

    def alert(self):
        alert = self.driver.switch_to.alert()
        return alert

    def explicitlyWait_ElementIsVisible(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def switchFrameUsingName(self, frameName):
        self.driver.switch_to.frmae(frameName)

    def switchFrameUsingId(self, frameId):
        self.driver.switch_to.frmae(frameId)

    def switchDefaultFrame(self):
        self.driver.switch_to_defaulr.content()





