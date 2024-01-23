from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def culc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    get_number = browser.find_element(By.ID, "input_value")
    got_number = get_number.text
    result = culc(got_number)

    text = browser.find_element(By.ID, "answer")
    text.send_keys(result)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
