from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()
finally:
    time.sleep(7)
    browser.quit()