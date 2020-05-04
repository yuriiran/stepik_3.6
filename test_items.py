import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_cart_button(browser):
    browser.get(link)
    #time.sleep(5)
    #проверяем если ли кнопка
    cart_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert cart_button, "should be a cart button"
    