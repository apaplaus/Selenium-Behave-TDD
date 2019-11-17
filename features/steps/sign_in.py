import os
import include
from include import web


#login: asdfasdf@gmail.com
#password: asdfasdf@gmail.com


@given ('page with sign in "<fields>" is displayed')
def step_impl(context):
    web.init_browser()
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=account/login")
    if web.is_logged_in():
        web.log_out()
    assert web.is_element_present(include.By.CSS_SELECTOR, "input#input-email")
    assert web.is_element_present(include.By.CSS_SELECTOR, "input#input-password")


@given ('user has account on site')
def step_impl(context):
    pass


@when ('user fills sign in "<fields>" with valid data')
def step_impl(context):
    email = web.driver.find_element_by_css_selector('input#input-email')
    email.clear()
    email.send_keys("asdfasdf@gmail.com")

    password = web.driver.find_element_by_css_selector('input#input-password')
    password.clear()
    password.send_keys("asdfasdf@gmail.com")
    password.submit()
    web.driver.find_element_by_xpath("//div[@id='content']/h2[text()='My Account']")

@then ('user signs in')
def step_impl(context):
    print(str(web.driver.current_url))
    assert str(web.driver.current_url).find("mys01.fit.vutbr.cz:8042/index.php?route=account/account") != -1



@then ('user have access to "<user pages>"')
def step_impl(context):
    my_acc_css = "#top-links li a[title='My Account']"
    web.driver.find_element_by_css_selector(my_acc_css).click()
    options = web.driver.find_element_by_css_selector(my_acc_css + " ~ ul")
    try:
        options.find_element_by_css_selector("a[href='http://mys01.fit.vutbr.cz:8042/index.php?route=account/account']")
        options.find_element_by_css_selector("a[href='http://mys01.fit.vutbr.cz:8042/index.php?route=account/order']")
        options.find_element_by_css_selector("a[href='http://mys01.fit.vutbr.cz:8042/index.php?route=account/transaction']")
        options.find_element_by_css_selector("a[href='http://mys01.fit.vutbr.cz:8042/index.php?route=account/download']")
    except include.NoSuchElementException as e:
        assert False
