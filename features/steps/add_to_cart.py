import os
import include
from include import web


@given("page of product displayed")
def step_impl(context):
    web.init_browser()
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=30")

@given('block with "Available Options" is representing')
def step_impl(context):
    assert "Available Options" in web.driver.page_source

@when('user completes all required fields')
def step_impl(context):
    select = include.Select(web.driver.find_element_by_css_selector('#product select'))
    select.select_by_index(1)

@then('user can add item to shopping cart')
def step_impl(context):
    web.driver.find_element_by_css_selector('#button-cart').click()
    assert "Success: You have added " in web.driver.page_source



product_count = 0

@given('user has logged in')
def step_impl(context):
    if not web.is_logged_in:
        web.sign_in_as("asdfasdf@gmail.com", "asdfasdf@gmail.com")

@given('page with desired product displayed')
def step_impl(context):
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=40")


@given('block "Available Options" is not present or filled up with valid data')
def step_impl(context):
    assert "Available Options" not in web.driver.page_source


@given('user has chosen quantity of product')
def step_impl(context):
    text = web.driver.find_element_by_css_selector('#input-quantity')
    text.clear()
    text.send_keys("1")


@when('user clicks on "Add to cart" button')
def step_impl(context):
    temp_text = web.driver.find_element_by_css_selector('#cart-total').text
    global product_count
    product_count = int(temp_text.split()[0])
    web.driver.find_element_by_css_selector('#button-cart').click()
    include.time.sleep(1)


@then('product adds to users cart')
def step_impl(context):
    temp_text = web.driver.find_element_by_css_selector('#cart').text
    global product_count
    count = int(temp_text.split()[0])
    assert count == product_count + 1


@then('field with notification about successful operation displayed')
def step_impl(context):
    assert "Success: You have added " in web.driver.page_source


@then('button representing shopping cart changes in accordance with the addition')
def step_impl(context):
    temp_text = web.driver.find_element_by_css_selector('#cart').text
    global product_count
    count = int(temp_text.split()[0])
    assert count == product_count + 1
