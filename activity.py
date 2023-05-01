from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/dynamic_controls')

prduct = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button').click()
driver.implicitly_wait(100)

prduct2 = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button').click()

wait = WebDriverWait(driver,10);
search = wait.until(EC.visibility_of_element_located((By.ID, 'message')))
