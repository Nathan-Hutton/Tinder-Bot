import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv('/Users/natha/PycharmProjects/info.env')

service = Service("C:\important\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://tinder.com/app/recs')
time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, 'a .l1xhyo4z')
login_button.click()
time.sleep(1)
facebook_button = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_button.click()
facebook_window = driver.window_handles[1]
base_window = driver.window_handles[0]
driver.switch_to.window(facebook_window)
email_button = driver.find_element(By.ID, 'email')
email_button.send_keys(os.getenv('EMAIL') + Keys.TAB + os.getenv('FACEBOOK_PASSWORD') + Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(4)
location_popup = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div/div/div[3]/button[1]')
location_popup.click()
notifications_popup = driver.find_element(By.XPATH, '//*[@id="s1659711021"]/div/div/div/div/div[3]/button[2]')
notifications_popup.click()
cookies_popup = driver.find_element(By.XPATH, '//*[@id="s-906875199"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies_popup.click()
time.sleep(3)
for i in range(100):
    time.sleep(3)
    try:
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_LEFT)
    except selenium.common.exceptions.NoSuchElementException:
        time.sleep(2)
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_LEFT)
