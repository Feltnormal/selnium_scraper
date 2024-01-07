import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options, FirefoxProfile
from _secrets import username, password
options = Options()
options.profile = FirefoxProfile("vtb1cawa.sel_user")
options.set_preference("media.eme.enabled", True)
options.set_preference("media.gmp-manager.updateEnabled", True)


def stream(user_creds: tuple):
    driver = webdriver.Firefox(options=options)  # expecting this to be in local repo
    driver.get("https://open.spotify.com/album/39hEC3Wb2aJCSpHYGjJ15Y?si=GKACjgF0RLSPij29rcMW8A")
    driver.implicitly_wait(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".LKFFk88SIRC9QKKUWR5u > button:nth-child(2)"))).click()

    driver.find_element("id", "login-username").send_keys(user_creds[0])
    driver.find_element("id", "login-password").send_keys(user_creds[1])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    # driver.find_element("id", "login-button").click()

    driver.implicitly_wait(5)

    # click top level play button and repeat button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='onetrust-close-btn-container']//button[@aria-label='Close']"))).click()
    # play song
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@data-testid='action-bar-row']//button[@data-testid='play-button' and @aria-label='Play']"))).click()
    # repeat enable
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]"))).click()

    # while True:
    #     # time.sleep(random.randint(30, 120))
    #     time.sleep(3)
    #     WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".mnipjT4SLDMgwiDCEnRC"))).click()


if __name__ == "__main__":
    with open('accounts.txt', 'r') as file:
       accounts = file.readlines()

    for account in accounts:
       stream(tuple(account.split(" ")))
