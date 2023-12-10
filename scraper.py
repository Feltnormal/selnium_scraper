from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

username = ""
password = ""

driver = webdriver.Firefox()
driver.get('https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F')
driver.implicitly_wait(5)

driver.find_element("id", "login-username").send_keys(username)
driver.find_element("id", "login-password").send_keys(password)
driver.find_element("id", "login-button").click()

driver.implicitly_wait(5)
