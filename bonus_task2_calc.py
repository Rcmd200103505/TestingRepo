from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://www.calculator.net/')
time.sleep(4)

number1 = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(3) > span:nth-child(1)")
plus = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(1) > span:nth-child(4)")
number2 = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(1) > span:nth-child(1)")
equals = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(5) > span:nth-child(4)")
minus = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(2) > span:nth-child(4)")
multiply = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(3) > span:nth-child(4)")
divide = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(4) > span:nth-child(4)")
back = driver.find_element(By.CSS_SELECTOR, "#sciout > tbody > tr:nth-child(2) > td:nth-child(2) > div > div:nth-child(1) > span:nth-child(5)")


driver.implicitly_wait(100)

actions = ActionChains(driver)

actions.click(number1).perform()
actions.click(plus).perform()
actions.click(number2).perform()
actions.click(equals).perform()
time.sleep(3)
testing = driver.find_element(By.ID, 'sciOutPut')
textt = testing.text
print(textt)
driver.implicitly_wait(10)
actions.click(back).perform()

time.sleep(3)

actions.click(number1).perform()
actions.click(minus).perform()
actions.click(number2).perform()
actions.click(equals).perform()
time.sleep(3)
testing = driver.find_element(By.ID, 'sciOutPut')
textt = testing.text
print(textt)
driver.implicitly_wait(10)
actions.click(back).perform()

time.sleep(3)

actions.click(number1).perform()
actions.click(multiply).perform()
actions.click(number2).perform()
actions.click(equals).perform()
time.sleep(3)
testing = driver.find_element(By.ID, 'sciOutPut')
textt = testing.text
print(textt)
driver.implicitly_wait(10)
actions.click(back).perform()

time.sleep(3)

actions.click(number1).perform()
actions.click(divide).perform()
actions.click(number2).perform()
actions.click(equals).perform()
time.sleep(3)
testing = driver.find_element(By.ID, 'sciOutPut')
textt = testing.text
print(textt)
driver.implicitly_wait(10)
actions.click(back).perform()

time.sleep(2)
