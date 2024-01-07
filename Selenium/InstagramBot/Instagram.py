from InstagramInfo import email,password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Instagram:
    def __init__(self,email,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome(options=self.browserProfile,service=ChromeService(ChromeDriverManager().install()))
        self.email = email
        self.password = password
        self.following = []

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        userEmail = self.browser.find_element("name","username")
        userEmail.send_keys(self.email)

        userPassword = self.browser.find_element("name","password")
        userPassword.send_keys(self.password)

        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(10)

        

    def getFollowing(self):

        self.browser.get(f"https://www.instagram.com/{self.email}")
        time.sleep(2)
        AccountInfolist = self.browser.find_elements(By.CSS_SELECTOR,'[class = "html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]')
        # followingCount = int(AccountInfolist[2].text)

    
        self.browser.get(f"https://www.instagram.com/{self.email}/following/")
        time.sleep(5)
        userfollowing = self.browser.find_elements(By.CSS_SELECTOR,'[class = "_ap3a _aaco _aacw _aacx _aad7 _aade"]')

        
        for items in userfollowing:
            self.following.append(items.text)
        
        with open('Followers.txt','w',encoding = "UTF-8") as file:
            for item in self.following:
                file.write(item +"\n")

    
        
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username+"/")
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text != 'Following':
            followButton.click()
            time.sleep(2)
        else:
            print("Your user is already being followed.")

    def unfollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username+"/")
        time.sleep(2)
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        followButton.click()
        
       
        if followButton.text == 'Following':
            time.sleep(2)
            # unfollowButton = self.browser.find_element(By.CSS_SELECTOR, '[class = "x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft"]')
            self.browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]").click()
            # unfollowButton.click()
            time.sleep(2)
        else:
            print("Your user is already being unfollowed.")
        

Insta = Instagram(email,password)
Insta.signIn()
Insta.getFollowing()
print(len(Insta.following))
inputFollow = input('Do you want to follow the user?')
if inputFollow == 'Yes' or inputFollow == 'YES':
    userName = input('Enter username : ')
    #followuserList = ["kod_evreni","uzunogluberna"] # şekilde liste ile kullalnlıcıları yazıp for döngüsü ile takip ettirebiliriz
    # for user in list:
    #     Insta.followUser(user)
    #     time.sleep(3)
    Insta.followUser(userName)
elif inputFollow == 'No' or inputFollow == 'NO':
    userName = input('Enter username : ')
    Insta.unfollowUser(userName)
else:
    print

