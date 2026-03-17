from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  os

try:
    # Сначала проверяем на первой ссылке, затем меняем на registration2.html для проверки бага
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля, используя уникальные связки классов
    # Поле First Name
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    # Поле Last Name
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    # Поле Email
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@mail.ru")

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ждем 10 секунд для визуального контроля и закрываем браузер
    time.sleep(10)
    browser.quit()