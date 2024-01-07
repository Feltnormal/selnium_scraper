import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options, FirefoxProfile
from _secrets import username, password
from multiprocessing import Pool, current_process
from multiprocessing import freeze_support

logging.basicConfig(level=logging.DEBUG)

options = Options()
options.profile = FirefoxProfile("vtb1cawa.sel_user")
options.set_preference("media.eme.enabled", True)
options.set_preference("media.gmp-manager.updateEnabled", True)


def run_multistream(func, i, n_processors):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, i)


# TODO: add proxy support
def stream(user_creds: str):
    username_key = user_creds.split(" ")[0]
    password_key = user_creds.split(" ")[1]
    logging.debug(f"{current_process().name} registering as user: {username_key}")
    driver = webdriver.Firefox(options=options)  # expecting this to be in local repo
    driver.get("https://open.spotify.com/album/39hEC3Wb2aJCSpHYGjJ15Y?si=GKACjgF0RLSPij29rcMW8A")
    driver.implicitly_wait(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".LKFFk88SIRC9QKKUWR5u > button:nth-child(2)"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-username"))).send_keys(username_key)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-password"))).send_keys(password_key)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

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

    # listen for random time greater than 35s and then skip to next song
    while True:
        time.sleep(random.randint(35, 120))
        logging.debug(f"{current_process().name} has elapsed wait time, skipping to next song")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".mnipjT4SLDMgwiDCEnRC"))).click()


if __name__ == "__main__":
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    freeze_support()
    out = run_multistream(stream, accounts, len(accounts))
