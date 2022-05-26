import allure
from selenium import webdriver


def before_feature(context, driver):
    print("Before Feature")


def before_scenario(context, driver):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--start-maximized')

    context.driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe", options=chrome_options)
    context.driver.delete_all_cookies()

def before_step(context, driver):
    print("Before step")

def before_tag(context, driver):
    pass

def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
