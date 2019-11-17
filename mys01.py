#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Remote Control
import selenium
from behave import *
import unittest, time, re

# WebDriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


#binary of browser
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class WebDriverFirefox(unittest.TestCase):
    def setUp(self):

        # self.driver = webdriver.Firefox(firefox_binary=FirefoxBinary(pathToBrowser))


        self.driver = webdriver.Firefox()


        # dp = {'browserName': 'firefox', 'marionette': 'true',
        #         'javascriptEnabled': 'true'}
        # self.driver = webdriver.Remote(
        #         command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
        #         desired_capabilities=dp)
#                desired_capabilities=DesiredCapabilities.FIREFOX)


        self.driver.implicitly_wait(30)
        self.base_url = "http://www.fit.vutbr.cz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_fit(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector("li:nth-child(2) > a > span").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
