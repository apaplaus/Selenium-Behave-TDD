#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Remote Control
import selenium
from behave import *
import time

# WebDriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


#binary of browser
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class WebDriverFirefox:
    driver = None

    def __init__(self):
        # self.driver = webdriver.Firefox(firefox_binary=FirefoxBinary(pathToBrowser))
        pass

    def init_browser(self):
        if not isinstance(self.driver, webdriver.Firefox):
            dp = {'browserName': 'firefox', 'marionette': 'true',
                    'javascriptEnabled': 'true'}
            self.driver = webdriver.Remote(
                    command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
                    desired_capabilities=dp)
                    # desired_capabilities=DesiredCapabilities.FIREFOX)

            # self.driver = webdriver.Firefox()

            self.driver.implicitly_wait(3)
            self.verificationErrors = []
            self.accept_next_alert = True
            self.driver.get("http://mys01.fit.vutbr.cz:8042/index.php?route=common/home")
            time.sleep(0.5)


    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def close_alert(self, accept = True):
        if self.is_alert_present():
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if accept:
                alert.accept()
            else:
                alert.dismiss()


    def open_url(self, url:str):
        self.close_alert()
        self.driver.get(url)
        self.close_alert()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True


    def sign_in_as(self, email:str, password:str):
        old_url = str(self.driver.current_url)
        self.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=account/login")

        email_el = self.driver.find_element_by_css_selector('input#input-email')
        email_el.clear()
        email_el.send_keys(email)

        password_el = self.driver.find_element_by_css_selector('input#input-password')
        password_el.clear()
        password_el.send_keys(password)
        password_el.submit()
        self.open_url(old_url)


    def is_cart_empty(self):
        time.sleep(0.5)
        cart_total = str(self.driver.find_element_by_css_selector("button:not(.disabled) #cart-total").text)
        return cart_total[0] == '0'


    def add_iphone_to_cart(self):
        old_url = str(self.driver.current_url)
        self.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=40")
        self.driver.find_element_by_id("button-cart").click()
        self.open_url(old_url)

    def is_logged_in(self):
        my_acc_css = "#top-links li a[title='My Account']"
        self.driver.find_element_by_css_selector(my_acc_css).click()
        ret = self.is_element_present(By.CSS_SELECTOR, my_acc_css + " ~ ul a[href='http://mys01.fit.vutbr.cz:8042/index.php?route=account/account']")
        return ret

    def log_out(self):
        old_url = str(self.driver.current_url)
        self.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=account/logout")
        self.open_url(old_url)


web = WebDriverFirefox()

if __name__ == "__main__":
    pass
