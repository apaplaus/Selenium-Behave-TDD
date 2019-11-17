import include
from include import web
import time



@given ('user has been logged in')
def step_impl(context):
    web.init_browser()
    if not web.is_logged_in():
        web.sign_in_as("asdfasdf@gmail.com", "asdfasdf@gmail.com")


@given ('shopping cart isn\'t empty')
def step_impl(context):
    web.add_iphone_to_cart()


@given ('"Checkout" page is displayed')
def step_impl(context):
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=checkout/checkout")
    #wait for page redirection
    time.sleep(1)


@given ('"Use new address" box is checked')
def step_impl(context):
    web.driver.find_element_by_xpath("//div[@id='collapse-payment-address']//label[input[@value='new' and @name='payment_address']]").click()

@when ('user fills up "<required fields>" with valid data')
def step_impl(context):
    form = web.driver.find_element_by_css_selector("#payment-new")
    inputs = form.find_elements_by_css_selector("#collapse-payment-address div.required input[type=text]")
    for  field, input in zip(context.active_outline, inputs) :
        input.send_keys(field)
    selects = form.find_elements_by_css_selector("#collapse-payment-address div.required select")
    for  field, select in zip(context.active_outline, selects) :
        include.Select(select).select_by_index(1)


@then ('next "Step" field opens')
def step_impl(context):
    web.driver.find_element_by_css_selector("#button-payment-address").click()
    assert web.is_element_present(include.By.CSS_SELECTOR, "#collapse-shipping-address[aria-expanded=\"true\"]")



@given ('steps 1, 2 and 3 in "Checkout" are completed')
def step_impl(context):
    assert web.is_element_present(include.By.CSS_SELECTOR, "#collapse-checkout-option.collapse")
    web.driver.find_element_by_css_selector("#collapse-payment-address.in[aria-expanded='true'] #button-payment-address").click()
    # assert web.is_element_present(include.By.CSS_SELECTOR, "#collapse-payment-address[aria-expanded='false']")
    web.driver.find_element_by_css_selector("#collapse-shipping-address.in[aria-expanded='true'] #button-shipping-address").click()
    # assert web.is_element_present(include.By.CSS_SELECTOR, "#collapse-shipping-address[aria-expanded='false']")
    assert web.is_element_present(include.By.CSS_SELECTOR, "#collapse-shipping-method.in[aria-expanded='true']")


@when ('user choose "Delivery Method"')
def step_impl(context):
    web.driver.find_element_by_css_selector("#collapse-shipping-method .radio label").click()
    web.driver.find_element_by_css_selector("#button-shipping-method").click()


@when ('choose "Payment Method" with confirmation of "Terms & Conditions"')
def step_impl(context):
    web.driver.find_element_by_css_selector("#collapse-payment-method.in .radio label").click()
    web.driver.find_element_by_css_selector("#collapse-payment-method input[name='agree']").click()
    web.driver.find_element_by_css_selector("#button-payment-method").click()



@when ('click "Confirm Order" button in "Step 6" box')
def step_impl(context):
    web.driver.find_element_by_css_selector("#collapse-checkout-confirm.in #button-confirm").click()


@then ('page with successful order placement displayed')
def step_impl(context):
    assert web.is_element_present(include.By.XPATH, "//div[@id='content']/h1[contains(text(),\"Your order has been placed!\")]")


@then ('shopping cart becomes empty')
def step_impl(context):
    assert web.is_cart_empty()


@then ('order adds to "Order History" user\'s page')
def step_impl(context):
    web.open_url("http://mys01.fit.vutbr.cz:8042/index.php?route=account/order")
    displayed_date = str(web.driver.find_element_by_css_selector("#content table tbody tr td:nth-child(6)").text)
    today_date = time.strftime(r"%d/%m/%Y")
    assert displayed_date.find(today_date) != -1
