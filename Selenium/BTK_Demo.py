# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.btkakademi.gov.tr"
driver.get(url) # verilen  adresi ziyaret eder.
time.sleep(2)

searchInput = driver.find_element("name", "q")
searchInput.send_keys("Python")
searchInput.send_keys(Keys.RETURN)
time.sleep(10)

# result = driver.page_source  # bu ifade ile sayfanın kaynak kodlarını bir değişken üzerine alıp değişken üzerinden etiketlere ulaşabiliriz.

result = driver.find_elements(By.CSS_SELECTOR,'[class="big-gray my-1"]')

for element in result: # elementin tag özelliklerinden text değerini alıcaz 
    print(element.text)


driver.close()