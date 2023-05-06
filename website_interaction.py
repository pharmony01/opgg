from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

def update_profile(url: str) -> None:
    # create a new Chrome browser instance
    driver = webdriver.Chrome()

    # navigate to the website
    driver.get(url)
    
    # Wait for page to load
    time.sleep(1)

    try:
        button = driver.find_element(By.CSS_SELECTOR, "button.my-button-class")
        button.click()
    except NoSuchElementException:
        print("Button not found!")

    # close the browser
    driver.quit()
