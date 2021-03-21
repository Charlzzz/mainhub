from selenium import webdriver
import time
import math
from math import log, sin
def calc(x):
  return str(log(abs(12*sin(int(x)))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    browser.implicitly_wait(7)
    button = WebDriverWait(browser, 7).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button = browser.find_element_by_id("book").click()
    browser.execute_script("window.scrollBy(0, 40);")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_id("solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    #browser.quit()