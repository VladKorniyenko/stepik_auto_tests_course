from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def sum(x, y):
    return str(x+y)


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    x = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    y = int(num2.text)

    answer = sum(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
