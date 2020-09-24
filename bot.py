from selenium import webdriver
import time
import os
from configparser import ConfigParser


class InstaBot:
    def __init__(self, username, passcode):
        self.username = username
        self.passcode = passcode
        self.url = "https://www.instagram.com/"
        self.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
        self.login_page()

    def login_page(self):
        self.driver.get("https://www.instagram.com/")
        u_name = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        u_name.send_keys(self.username)
        key = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        key.send_keys(self.passcode)
        log_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
        log_btn.click()

    def nav_user(self, user):
        self.driver.get('{}{}/'.format(self.url, user))

    def search_user(self, user1):
        search = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(user1)

    def follow_account(self, user):
        self.nav_user(user)
        f_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
        f_btn.click()


if __name__ == '__main__':
    parser = ConfigParser()
    parser.read('cinfig.ini')
    username = parser['AUTH']['username']
    passcode = parser['AUTH']['password']
    igBot = InstaBot(username, passcode)
    # time.sleep(7)
    # igBot.follow_account('narendramodi')
    # time.sleep(15)
    # igBot.search_user('amitshahofficial')
    # igBot.follow_account('amitshahofficial')
    # user2 = input("ENter the Insta ID===  ")
    # igBot.search_user(user2)
    # time.sleep(10)
    # igBot.follow_account(user2)
