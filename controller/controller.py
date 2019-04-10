import os
from selenium import webdriver


class Controller(object):

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, browser):
        if browser == 'firefox':
            self.driver = webdriver.Firefox(executable_path='/Users/ilionailiadhi/Ora/automation-project/geckodriver')
        elif browser == 'chrome':
            self.driver = webdriver.Chrome('{}/chromedriver'.format(os.getcwd()))

    def input_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def quit_driver(self):
        self.driver.quit()
