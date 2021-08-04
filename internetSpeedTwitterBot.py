from selenium import webdriver
import time

PATH = "C:/Development/chromedriver.exe"
SPEED_SITE = "https://www.speedtest.net/"
TWITTER_SITE = "https://twitter.com/login"
USER = "" #Your username
PASS = "" #Your password


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.down = 0
        self.up = 0
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get(SPEED_SITE)
        start = self.driver.find_element_by_css_selector(".start-button a .start-text")
        start.click()
        time.sleep(10)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        if float(self.down) < 1 or float(self.up) < 0.50:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_SITE)
        time.sleep(5)
        user_name = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user_name.click()
        user_name.send_keys(USER)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.click()
        password.send_keys(PASS)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span')
        login.click()
        time.sleep(3)
        post = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div')
        post.click()
        post.send_keys(f"Hey Yemen net, why my my internet speed {self.down}down/{self.up}up when I pay for 2down/0.50up?")
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()
