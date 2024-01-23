from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def culc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    got_number = x.text
    answer = culc(got_number)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer)

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
