from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
import pytest

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://shop.kz/')
    driver.implicitly_wait(10)
    assert "lkemflkm" in driver.title

def test_search():
    search = driver.find_element(By.CLASS_NAME, 'search-hover__submit').click()
    driver.implicitly_wait(10)
    search = driver.find_element(By.CLASS_NAME, 'multi-input')
    search.send_keys("a4tech")
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    assert driver.title == "Интернет-магазин Белый Ветер"

def test_product_button():
    prduct = driver.find_element(By.XPATH, "//*[contains(@data-product, '1005024')]").click()
    driver.implicitly_wait(10)

def test_add_product():
    buy = driver.find_element(By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]').click()
    driver.implicitly_wait(10)
    backet = driver.find_element(By.XPATH, '//*[@id="bx_117848907_1005024_add_basket_link"]').click()
    driver.implicitly_wait(10)

def test_homepage():
    homepage = driver.find_element(By.XPATH, '//*[@id="bx_eshop_wrap"]/header/div/div/div[1]/div/a[1]/img').click()
    driver.implicitly_wait(10)

def test_backet():
    backett = driver.find_element(By.NAME, 'splash-button').click()
    driver.implicitly_wait(10)

def test_delete_item():
    delete = driver.find_element(By.CLASS_NAME, 'cart__rem-item').click()
    driver.implicitly_wait(10)

def test_shop_title():
    assert driver.title in "Интернет-магазин"

def test_shop_url():
    assert driver.url







