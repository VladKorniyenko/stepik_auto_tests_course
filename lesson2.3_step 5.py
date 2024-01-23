from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def culc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    get_value = browser.find_element(By.ID, "input_value")
    got_value = get_value.text
    answer = culc(got_value)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
