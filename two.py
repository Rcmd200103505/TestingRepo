from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://intertop.kz/')
time.sleep(4)

maga = driver.find_element(By.CLASS_NAME, 'input')
time.sleep(4)

maga.send_keys("nike")
maga.send_keys(Keys.ENTER)
time.sleep(5)


maga2 = driver.find_element(By.CLASS_NAME, 'new-product__new-price').click()
time.sleep(7)

maga3 = driver.find_element(By.CLASS_NAME, 'size-picker').click()
time.sleep(7)


maga4 = driver.find_element(By.XPATH, "//*[contains(@data-product, '1116744')]").click()
time.sleep(7)


maga5 = driver.find_element(By.XPATH, "//*[contains(@class, 'btn js-element-add-to-basket success custom-product-basket-added')]").click()
time.sleep(5)