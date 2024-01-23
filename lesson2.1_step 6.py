from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.TAG_NAME, "img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
