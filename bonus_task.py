from selenium import webdriver
#import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time


driver = webdriver.Chrome()
driver.get('https://accounts.google.com/ServiceLogin/identifier?service=wise&passive=1209600&osid=1&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Fu%2F0%2Fmy-drive&ifkv=AWnogHcb5W8SjPZbNjefG-r3KFxMMbH-ESZtd2cyvNyb6qy4nvfs9v9BF66woRNaQZzRqmK0FrE3Tg&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(3)
wait = WebDriverWait(driver, 10)
login = driver.find_element(By.XPATH, "//*[contains(@class, 'whsOnd zHQkBf')]")
login = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'whsOnd zHQkBf')]")))
login.send_keys('200103505@stu.sdu.edu.kz')
time.sleep(5)
login.send_keys(Keys.ENTER)
time.sleep(9)

password = driver.find_element(By.XPATH, "//*[contains(@class, 'whsOnd zHQkBf')]")
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'whsOnd zHQkBf')]")))
password.send_keys('22996254AE86')
password.send_keys(Keys.ENTER)
#driver.implicitly_wait(100)



time.sleep(5)
basket1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-tooltip,'8 march MK 2022')]")))
#basket1 = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'8 march MK 2022')]")
basket2 = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'7 may MK 2022')]")
action = ActionChains(driver)
action.drag_and_drop(basket1, basket2).perform()

time.sleep(5)

okk = driver.find_element(By.XPATH, "//*[contains(@class,'h-De-Vb h-De-Y a-X-d')]").click()
time.sleep(5)
click = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'7 may MK 2022')]")
action.double_click(click).perform()

time.sleep(5)

ax = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'8 march MK 2022')]")
ok2 = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'My Drive')]")

action.drag_and_drop(ax, ok2).perform()

time.sleep(5)

okk = driver.find_element(By.XPATH, "//*[contains(@class,'h-De-Vb h-De-Y a-X-d')]").click()

time.sleep(5)

ok2 = driver.find_element(By.XPATH, "//*[contains(@data-tooltip,'My Drive')]").click()

time.sleep(5)





