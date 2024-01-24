from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contain_add_button_to_basket(browser):
    browser.get(link)
    # time.sleep(30)
    cart_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    class_cart_button = cart_button.get_attribute("class")
    assert "btn-add-to-basket" in class_cart_button, "There is no add to cart button"
