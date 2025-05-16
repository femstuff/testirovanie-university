from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
time.sleep(1)

browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

assert "Sauce Labs Backpack" in browser.page_source

browser.find_element(By.ID, "checkout").click()
time.sleep(1)

browser.find_element(By.ID, "first-name").send_keys("Мальбо")
browser.find_element(By.ID, "last-name").send_keys("Мальбов")
browser.find_element(By.ID, "postal-code").send_keys("62500")
browser.find_element(By.ID, "continue").click()
time.sleep(1)

browser.find_element(By.ID, "finish").click()
time.sleep(1)

assert "Thank you for your order!" in browser.page_source
print("Success")

time.sleep(5)
browser.quit()