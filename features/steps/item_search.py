import include
from include import web
import os



@given ('store main page is displayed')
def step_impl(context):
    web.init_browser()
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=common/home")

@when ('user click on "<category>" and choose paragraph with desired item')
def step_impl(context):
    web.driver.find_element_by_css_selector("#menu ul > li:nth-child(3)").click()
    web.driver.find_element_by_css_selector("#menu ul > li:nth-child(3) ul > li:nth-child(2)").click()

@then ('first page with items of chosen "<category>" paragraph displayed')
def step_impl(context):
    assert web.driver.current_url == "http://mys01.fit.vutbr.cz:8042/index.php?route=product/category&path=25_28"
