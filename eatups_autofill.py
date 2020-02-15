from selenium import webdriver
import numpy as np
import pandas as pd

class eatupsbot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login():
        self.driver.get('https://forms.gle/cVaqVfVbLXQCRRqKA')

        sleep(2)

        # gmail login
        gmail_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        gmail_input.send_keys('*@stonybrook.edu')

        gmail_input_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        gmail_input_button.click()

        # net id login
        netid = self.driver.find_element_by_xpath('//*[@id="username"]')
        netid_password = bot.driver.find_element_by_xpath('//*[@id="password"]')
        netid_login = bot.driver.find_element_by_xpath('//*[@id="main-form-inputs"]/div[5]/button')

        netid.send_keys('***')
        netid_password.send_keys('***')
        sleep(1)
        netid_login.click()

        recognize_cont_btn = bot.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div')
        recognize_cont_btn.click()
        sleep(1)

        building = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
        building.click()
        sleep(0.5)

        name = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        name.send_keys('***')

        month = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
        day = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div[1]/input')
        month.send_keys('02')
        day.send_keys('02')

        dining_facility = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[11]/label/div/div[1]/div/div[3]/div')
        dining_facility.click()

        visit = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
        visit.click()

        names = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input')
        names.send_keys('myself')
        submit = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[2]/div/div/span')
        submit.click()

        another_response = bot.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response.click()
