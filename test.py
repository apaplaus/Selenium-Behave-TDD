#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary(pathToBrowser)
# driver = webdriver.Firefox(firefox_binary=binary)



driver = webdriver.Firefox()
driver.get("https://www.python.org/")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
