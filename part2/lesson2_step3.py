import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = num1.text

    num2 = browser.find_element(By.ID, "num2")
    y = int(num2.text) + int(x)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{y}")

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
