
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://github.com/BernaUzunoglu"
driver.get(url) # verilen  adresi ziyaret eder.

time.sleep(2)
driver.maximize_window() # açılan sayfayı büyütüyor

print(driver.title)

if "BernaUzunoglu" in driver.title:
    driver.save_screenshot("github.com - Homepage.png")
    
time.sleep(2)
driver.close()