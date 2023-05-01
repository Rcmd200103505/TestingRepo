from selenium import webdriver
import undetected_chromedriver as uc
browser = uc.Chrome()
browser.get('https://accounts.google.com/AccountChooser?service=writely')