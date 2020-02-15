from selenium import webdriver
import numpy as np
import pandas as pd
from time import sleep

class eatupsbot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def readfile(self):
        raw_data = pd.read_csv("eatups.csv")
        return raw_data

    def select_dining_facility(self, dining_facility):
        East = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
        GLS = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
        Hospital = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div')

        Jasmine = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div')
        Roth = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
        SAC = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[6]/label/div/div[1]/div/div[3]/div')

        Simons_cafe = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[7]/label/div/div[1]/div/div[3]/div')
        Strbks_lib = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[8]/label/div/div[1]/div/div[3]/div')
        Strbks_rth = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[9]/label/div/div[1]/div/div[3]/div')

        TAC = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[10]/label/div/div[1]/div/div[3]/div')
        West = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[11]/label/div/div[1]/div/div[3]/div')
        Other = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[12]/div/label/div/div[1]/div/div[3]/div')
        other_text = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[12]/div/div/span/div/div/div[1]/input')

        # print('\n******************' + dining_facility + '********************\n')

        if dining_facility == "East" :
            return_facility = East
        elif dining_facility == "GLS" :
            return_facility = GLS
        elif dining_facility == "Hospital" :
            return_facility = Hospital
        elif dining_facility == "Jasmine" :
            return_facility = Jasmine
        elif dining_facility == "Roth" :
            return_facility = Roth
        elif dining_facility == "SAC" :
            return_facility = SAC
        elif dining_facility == "Simons Cafe" :
            return_facility = Simons_cafe
        elif dining_facility == "Starbucks - Library" :
            return_facility = Strbks_lib
        elif dining_facility == "Starbucks - Roth" :
            return_facility = Strbks_rth
        elif dining_facility == "TAC" :
            return_facility = TAC
        elif dining_facility == 'West' :
            return_facility = West
        else :
            return_facility = Other
            other_text.send_keys(dining_facility)

        return return_facility

    def fillform(self, d):

        date = d[0]
        dining_facility = d[1]
        description = d[2]
        resident_names = d[3]

        # Starting to fill the form
        building = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
        building.click()
        sleep(1)

        name = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        name.send_keys('***')


        month = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
        day = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div[1]/input')
        dates = date.split('/')
        month.send_keys(dates[0])
        day.send_keys(dates[1])
        sleep(1)

        dining_facility = self.select_dining_facility(dining_facility)
        dining_facility.click()
        sleep(1)

        # visit
        single_res = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
        mult_rest = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')

        if ("," or "and") in resident_names:
            mult_rest.click()
        else:
            single_res.click()
        sleep(1)

        names = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[1]/input')
        names.send_keys(resident_names)
        sleep(1)

        submit = bot.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[2]/div/div/span')
        submit.click()

    def another_response(self):
        sleep(0.5)
        another_response = bot.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response.click()

    def login(self):
        self.driver.get('https://forms.gle/cVaqVfVbLXQCRRqKA')

        sleep(1)

        # gmail login
        gmail_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        gmail_input.send_keys('***@stonybrook.edu')

        gmail_input_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        gmail_input_button.click()

        # self.driver.switch_to_window(self.driver.window_handles[0])
        # self.driver.switch_to.active_element()
        sleep(2)
        # print("\n****************************************************************\n")

        # net id login
        netid = self.driver.find_element_by_xpath('//*[@id="username"]')
        netid_password = bot.driver.find_element_by_xpath('//*[@id="password"]')
        netid_login = bot.driver.find_element_by_xpath('//*[@id="main-form-inputs"]/div[5]/button')

        netid.send_keys('***')
        netid_password.send_keys('***')
        sleep(2)
        netid_login.click()

        recognize_cont_btn = bot.driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div')
        recognize_cont_btn.click()
        sleep(1)

        data = self.readfile()

        for i in range(len(data)):
            d=[]
            for each in data:
                d.append(data[each][i])

            self.fillform(d)
            self.another_response()


bot = eatupsbot()
bot.login()
