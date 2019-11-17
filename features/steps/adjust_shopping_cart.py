import include
import time
from include import web

total_price = 0
item_total_price = 0

def get_total_price():
    if web.is_cart_empty():
        return None
    if web.is_element_present(include.By.XPATH, "//td[strong[text()='Total:']]/following-sibling::td"):
        return float(str(web.driver.find_element_by_xpath("//td[strong[text()='Total:']]/following-sibling::td").text)[1:].replace(',',''))
    return None


def get_item_total_price():
    if web.is_cart_empty():
        return None
    if web.is_element_present(include.By.CSS_SELECTOR, "#content > form table > tbody > tr > td:nth-child(6)"):
        return float(str(web.driver.find_element_by_css_selector("#content > form table > tbody > tr > td:nth-child(6)").text)[1:].replace(',',''))
    return None


@given ('"Shopping cart" page is displayed')
def step_impl(context):
    web.init_browser()
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=checkout/cart")



@when ('user changes "Quantity" field in row with appropriate product')
def step_impl(context):
    elem = web.driver.find_element_by_css_selector("#content > form table > tbody > tr > td:nth-child(4) input[type='text']")
    quantity = str(elem.get_attribute("value"))
    elem.clear()
    quantity = str(int(quantity) + 1)
    elem.send_keys(quantity)


@when ('press "Update" button')
def step_impl(context):
    global total_price
    global item_total_price
    total_price = get_total_price()
    item_total_price = get_item_total_price()
    web.driver.find_element_by_css_selector("#content > form table > tbody > tr > td:nth-child(4) button[type='submit']").click()


@then ('page reloads')
def step_impl(context):
    #wait for reload completes
    time.sleep(1)


@then ('"Total" price for this item changes')
def step_impl(context):
    assert item_total_price != get_item_total_price()


@then ('"Total" price for all items in cart changes')
def step_impl(context):
    assert total_price != get_total_price()


items_amount = 0


@given ('shopping cart has more than one product')
def step_impl(context):
    web.add_iphone_to_cart()
    time.sleep(1)
    old_url = str(web.driver.current_url)
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=product/product&product_id=43")
    web.driver.find_element_by_id("button-cart").click()
    web.open_url(old_url)
    time.sleep(1)


@when ('user press "Remove" button on appropriate product')
def step_impl(context):
    global total_price
    global items_amount
    items_amount = len(web.driver.find_elements_by_css_selector("#content > form table > tbody > tr "))
    total_price = get_total_price()
    print("items_amount: {}".format(items_amount))
    print("total_price: {}".format(total_price))
    print("current url: {}".format(web.driver.current_url))
    web.driver.find_element_by_css_selector("#content > form table > tbody > tr > td:nth-child(4) button[type='button']").click()
    time.sleep(1)


@then ('field with notification about successful deletion displayed')
def step_impl(context):
    assert web.is_element_present(include.By.CSS_SELECTOR, "div.alert.alert-success")


@then ('item removed from shopping cart')
def step_impl(context):
    assert items_amount == (len(web.driver.find_elements_by_css_selector("#content > form  table > tbody > tr ")) + 1)



@given ('shopping cart has one product')
def step_impl(context):
    if(web.is_cart_empty()):
        web.add_iphone_to_cart()

    while len(web.driver.find_elements_by_css_selector("#content > form  table > tbody > tr ")) > 1:
        web.driver.find_element_by_css_selector("#content > form table > tbody > tr > td:nth-child(4) button[type='button']").click()
        time.sleep(0.5)


@then ('page with empty shopping cart is displayed')
def step_impl(context):
    print("current utl : " + web.driver.current_url)
    print("is cart empty: " + str(web.is_cart_empty()))
    assert web.is_cart_empty() and str(web.driver.current_url).find("mys01.fit.vutbr.cz:8042/index.php?route=checkout/cart") != -1
