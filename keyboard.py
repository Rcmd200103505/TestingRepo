from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://gate2home.com/English-Keyboard')
time.sleep(4)

caps = driver.find_element(By.ID, 'kb_bcaps')
capital_a = driver.find_element(By.ID, 'kb_b26')
caps = driver.find_element(By.ID, 'kb_bcaps')
u = driver.find_element(By.ID, 'kb_b20')
t = driver.find_element(By.ID, 'kb_b18')
o = driver.find_element(By.ID, 'kb_b22')
m = driver.find_element(By.ID, 'kb_b43')
a = driver.find_element(By.ID, 'kb_b26')
t = driver.find_element(By.ID, 'kb_b18')
i = driver.find_element(By.ID, 'kb_b21')
o = driver.find_element(By.ID, 'kb_b22')
n = driver.find_element(By.ID, 'kb_b42')
space = driver.find_element(By.XPATH, '//*[@id="kb_bspace"]')
i = driver.find_element(By.ID, 'kb_b21')
n = driver.find_element(By.ID, 'kb_b42')
space = driver.find_element(By.XPATH, '//*[@id="kb_bspace"]')
t = driver.find_element(By.ID, 'kb_b18')
e = driver.find_element(By.ID, 'kb_b16')
s = driver.find_element(By.ID, 'kb_b27')
t = driver.find_element(By.ID, 'kb_b18')
i = driver.find_element(By.ID, 'kb_b21')
n = driver.find_element(By.ID, 'kb_b42')
g = driver.find_element(By.ID, 'kb_b30')
driver.implicitly_wait(100)

actions = ActionChains(driver)
actions.click(caps).perform()
actions.click(capital_a).perform()
actions.click(caps).perform()
actions.click(u).perform()
actions.click(t).perform()
actions.click(o).perform()
actions.click(m).perform()
actions.click(a).perform()
actions.click(t).perform()
actions.click(i).perform()
actions.click(o).perform()
actions.click(n).perform()
actions.click(space).perform()
actions.click(i).perform()
actions.click(n).perform()
actions.click(space).perform()
actions.click(t).perform()
actions.click(e).perform()
actions.click(s).perform()
actions.click(t).perform()
actions.click(i).perform()
actions.click(n).perform()
actions.click(g).perform()

time.sleep(4)

testing = driver.find_element(By.XPATH, '//*[@aria-label="Text Area"]')
textt = testing.text


print(textt)
