import include
from include import web
import os


@given('user have seen block with link to certain product on store page')
def step_impl(context):
    web.init_browser()
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=common/home")
    assert "iPhone" in web.driver.page_source
    assert web.is_element_present(include.By.XPATH, '//div[@class="image"]/a[@href="http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=40"]')

@when('user clicks link with product')
def step_impl(context):
    web.driver.find_element_by_xpath('//div[@class="image"]/a[@href="http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=40"]').click()


@then('page with detailed information about product displayed')
def step_impl(context):
    assert web.is_element_present(include.By.CSS_SELECTOR, '#tab-description')

@then('block with purchase information displayed')
def step_impl(context):
    assert web.is_element_present(include.By.CSS_SELECTOR, '#product')
