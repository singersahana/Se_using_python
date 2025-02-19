import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

search_text_box =driver.find_element(By.CLASS_NAME,"gLFyf")
search_text_box.send_keys("Automation")
search_text_box.send_keys(Keys.RETURN)
print("successfully entered!!")
# time.sleep(2)
# driver.find_element(By.NAME,"btnK").click()
time.sleep(2)
# print("successfully entered!!")
# driver.close()
