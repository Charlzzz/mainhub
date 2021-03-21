from selenium import webdriver
import time
# импортируем модуль
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)


    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("sergei")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("kuzin")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("sss@yandex.ru")
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
     # имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_name("file")
    # отправляем файл
    element.send_keys(file_path)
    button = browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()