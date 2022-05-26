import time

from behave import *

from Pageobjects.HomePage import HomePage
from Pageobjects.LoginPage import LoginPage
from Utilities.Reusable import Reusable_functions


@given(u'user launch browser')
def step_impl(context):
    context.hp = HomePage(context.driver)

    context.hp.open("https://rahulshettyacademy.com/angularpractice/")
    context.util = Reusable_functions(context.driver)
    context.util.type(context.hp.name_item(), "Mahesh1234")
    time.sleep(2)


@given(u'User login to "{URL}" webpage')
def step_impl(context, URL):

    context.util = Reusable_functions(context.driver)
    context.util.openBrowser(URL)
    print(context.util.getTitle())

    assert "Llogin" in context.util.getTitle()



@when(u'user enters email as "{email}" and password a "{password}"')
def step_impl(context, email, password):
    context.lp = LoginPage(context.driver)
    context.util = Reusable_functions(context.driver)

    context.util.type(context.lp.get_Email(),email)
    context.util.type(context.lp.get_Password(), password)
    context.util.click(context.lp.get_LoginButton())





@when(u'Customer submenu selected')
def step_impl(context):
    context.util = Reusable_functions(context.driver)
    context.hp = HomePage(context.driver)

    context.util.click(context.hp.get_CustomerMenu())
    context.util.click((context.hp.get_CustomerSubMenu()))





@when(u'Add new button clicked')
def step_impl(context):
    context.util = Reusable_functions(context.driver)
    context.hp = HomePage(context.driver)

    context.util.click(context.hp.get_AddNew())






@when(u'All Customer details entered')
def step_impl(context):
    pass


@then(u'customer record created successfully')
def step_impl(context):
    pass
