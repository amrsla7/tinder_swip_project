from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException , ElementNotInteractableException , StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import time
import random


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service() , options=options)

driver.get("https://tinder.com/")
main_page = driver.current_window_handle
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Log in").click()

time.sleep(4)

while True:
    try:
        phone_number_field = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button").click()
        break
    except NoSuchElementException:
        time.sleep(5)
while True:
    try:
        phone_number_field = driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/input")
        phone_number_field.send_keys("1010683958")
        phone_number_field.send_keys(Keys.ENTER)
        break
    except NoSuchElementException:
        print("no number yet")
        time.sleep(5)
while True:
    try:
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button").click()
    except (ElementClickInterceptedException,ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException,StaleElementReferenceException):
        try:
            driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div[2]/button[2]").click()
        except (ElementClickInterceptedException,ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException,StaleElementReferenceException):
            try:
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div/button[2]").click()
            except (ElementClickInterceptedException, ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException,StaleElementReferenceException):
                time.sleep(5)
    time.sleep(random.randint(1,2))






