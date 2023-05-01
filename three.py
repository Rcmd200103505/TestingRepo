from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://shop.kz/')


wait = WebDriverWait(driver, 10)


search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-hover__submit')))
search.click()


search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'multi-input')))
search.send_keys("a4tech")
search.send_keys(Keys.ENTER)


product = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-product, '1005024')]")))
product.click()

#buy = driver.find_element(By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]').click()
buy = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]')))
buy.click()

#basket = driver.find_element(By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]').click()
basket = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]')))
basket.click()

#homepage = driver.find_element(By.XPATH, '//*[@id="bx_eshop_wrap"]/header/div/div/div[1]/div/a[1]/img').click()
homepage = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_eshop_wrap"]/header/div/div/div[1]/div/a[1]/img')))
homepage.click()

#backett = driver.find_element(By.NAME, 'splash-button').click()
backett = wait.until(EC.element_to_be_clickable((By.NAME, 'splash-button')))
backett.click()

#delete = driver.find_element(By.CLASS_NAME, 'cart__rem-item').click()
delete = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'cart__rem-item')))
delete.click()

time.sleep(5)







