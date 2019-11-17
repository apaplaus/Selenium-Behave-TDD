from include import web

def after_all(context):
    web.driver.quit()
