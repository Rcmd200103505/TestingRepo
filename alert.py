from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Alerts.html')
time.sleep(4)

red = driver.find_element(By.XPATH, '//*[@class="btn btn-danger"]').click()
time.sleep(3)
alertt = driver.switch_to.alert
time.sleep(3)
alertt.accept()
time.sleep(3)

ok = driver.find_element(By.CSS_SELECTOR, 'body > div.container.center > div > div > div > div.tabpane.pullleft > ul > li:nth-child(2) > a').click()
time.sleep(3)
blue = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
time.sleep(3)
alertt.accept()



time.sleep(4)






