from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def culc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()

    get_value = browser.find_element(By.ID, "input_value")
    x = get_value.text
    answer = culc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
