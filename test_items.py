import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_cart_button(browser):
    browser.get(link)
    time.sleep(5)
    #проверяем если ли кнопка
    cart_button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert cart_button, "should be a cart button"
    