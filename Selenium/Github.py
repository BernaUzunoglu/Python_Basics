from GithubUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Github:
   
    def __init__(self,username,password):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.username = username
        self.password = password
        self.followers = []
        self.profilName = ""
        
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        searhUsername = self.browser.find_element("name", "login")
        searhUsername.send_keys(self.username)

        searhPassword = self.browser.find_element("name","password")
        searhPassword.send_keys(self.password)

        buttonSignin = self.browser.find_element("name","commit")
        buttonSignin.click()
        time.sleep(10)
        
        self.browser.get("https://github.com/")
        profilButton = self.browser.find_element(By.CSS_SELECTOR,'[class = "avatar circle"]')
        profilButton.click()
        time.sleep(2)
        linkUsername = self.browser.find_element(By.CSS_SELECTOR,'[class = "Truncate-text"]')
        self.profilName = linkUsername.text


    def getFollwers(self):
        self.browser.get(f"https://github.com/{self.profilName}?tab=followers")
        time.sleep(2)
        followersItems = self.browser.find_elements(By.CSS_SELECTOR,'[class = "d-inline-block"]')
        for items in followersItems:
            self.followers.append(items.accessible_name[1:])


Git = Github(username,password)
Git.signIn()
Git.getFollwers()
for items in Git.followers:
    print(items)


