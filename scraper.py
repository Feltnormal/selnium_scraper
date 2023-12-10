from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

username = ""
password = ""

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()  # expecting this to be in local repo
driver.get('https://open.spotify.com/track/0WSEq9Ko4kFPt8yo3ICd6T?si=e2c993506d17435b&nd=1')
driver.implicitly_wait(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".LKFFk88SIRC9QKKUWR5u > button:nth-child(2)"))).click()

driver.find_element("id", "login-username").send_keys(username)
driver.find_element("id", "login-password").send_keys(password)
driver.find_element("id", "login-button").click()

driver.implicitly_wait(5)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='onetrust-close-btn-container']//button[@aria-label='Close']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='action-bar-row']//button[@data-testid='play-button' and @aria-label='Play']"))).click()
