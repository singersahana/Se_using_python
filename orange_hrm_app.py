import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
Username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
Username.send_keys("Admin")
Password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
Password.send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(3)
