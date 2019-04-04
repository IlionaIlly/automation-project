from behave import *
from controller.controller import Controller


@step('I open the browser')
def open_chrome(context):
    context.controller = Controller(driver=None)
    context.controller.open_chrome()


@step('I type the url "{url}" in the address bar')
def input_url(context, url):
    context.controller.input_url(url)


@step('I verify the "{title}" is displayed')
def verify_facebook(context, title):
    assert title == context.controller.get_title()


@step('I quit the browser')
def quit_browser(context):
    context.controller.quit_driver()
