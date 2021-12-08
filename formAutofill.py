# title          : formAutofill.py
# description    : Python Script to automate emails to U.S. Senators
# author         : Daniel Brett
# date           : November 20th, 2018
# python_version : 3.6
# ==================================================

#Relevant libraries for automating web form filling
import schedule
import time
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import random
import fileinput

class AutomateForm(object):

    def __init__(self, url):
        self.url = url


    def replace_word(self, file, senatorName):
        in_file = open("messageTemplates/"+file, "rt")
        contents = in_file.read()
        in_file.close()
        edited_version = ''
        for line in contents:
            if line!='_':
                edited_version+=line
            else:
                edited_version+=senatorName
        return edited_version




    def autoFillCollins(self):
        #Send Ten emails, one each hour. Values can be adjusted to annoy representatives if needed.
        for x in range(10):
            #Open a new browser w/ Collins URL
            driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
            driver.get(self.url)

            #Upload the normal fields
            xpath_dict = {'//*[@id="edit-submitted-first-name"]': 'John', '//*[@id="edit-submitted-last-name"]':'Smith', '//*[@id="edit-submitted-address-1"]':'123 Raindbow Street', '//*[@id="edit-submitted-city-town"]':'Portland', '//*[@id="edit-submitted-zip-code"]':'04106', '//*[@id="edit-submitted-e-mail"]': 'johnsmith@gmail.com'}
            for key in xpath_dict:
                box = driver.find_element_by_xpath(key)
                box.send_keys(xpath_dict[key])

            #Fill in radio buttons - do NOT subscribe and currently not asking for a response
            driver.find_elements_by_css_selector("input[type = 'radio'][value = 'No']")[1].click()

            #Fill in State dropdown
            mySelect = Select(driver.find_element_by_id('edit-submitted-state'))
            mySelect.select_by_visible_text('Maine')

            #Fill in Message from message bank by randomly selecting which file/message to send
            stringNum = str(random.randint(0,1))
            myFile = "genMessage"+stringNum+".txt"

            #Parse actual file & load message into variable

            contents = self.replace_word(myFile, "Collins")
            message_box = driver.find_element_by_xpath('//*[@id="edit-submitted-please-write-your-message"]')
            message_box.send_keys(unicode(contents, errors = 'ignore'))


            #pause for an hour
            time.sleep(3600)


        #Submit all information - uncomment this line in order to submit information from files
        #submit_button = driver.find_element_by_xpath('//*[@id="webform-client-form-9020"]/div/div[16]/input')
        #submit_button.click()

    def autoFillKing(self):
        #Similar layout where 10 emails are sent, one each hour
        for x in range(10):
            #open a new browser w/ King URl
            driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
            driver.get(self.url)

            #upload all required fields that have short answer
            xpath_dict = {'//*[@id="input-EFEFBB82-E5AD-43BF-317C-6365EAD5F540"]':'John', '//*[@id="input-EFEFBC04-A1C6-A99B-E17A-465BF19BB596"]': 'Smith', '//*[@id="input-EFF6FADA-AC70-B16D-6B17-9B9B5EB61A8B"]': '123 Rainbow Street', '//*[@id="input-EFF6FC50-9F27-52E9-FC8A-9E973337F5A7"]': 'South Portland', '//*[@id="input-EFF6FE05-FD47-9CAE-592B-DD721DE754D5"]': '04106', '//*[@id="input-EFF948B7-026A-A6A4-00B1-846C8E5E9C5B"]': '2079998888', '//*[@id="email"]': 'johnsmith@gmail.com', '//*[@id="input-C7C6BFDA-A10F-8024-D3ED-889AC2304F7D"]': 'johnsmith@gmail.com'}
            for key in xpath_dict:
                box = driver.find_element_by_xpath(key)
                box.send_keys(xpath_dict[key])

            #upload required fields that have dropdown menus
            myState = Select(driver.find_element_by_id('input-EFF6FD8D-9A59-4FE6-D179-F465F1938DF2'))
            myState.select_by_visible_text('ME')

            myIssue = Select(driver.find_element_by_id("input-EFFE74ED-C7CC-D044-49D2-3B1B3C8DC9F8"))
            myIssue.select_by_visible_text('Defense & Intelligence')

            #Will need to change this to be more dynamic depending on messages
            message_subject = driver.find_element_by_xpath('//*[@id="input-3E2E3A97-EC40-4905-D23E-5027DF4B2878"]')
            message_subject.send_keys('Concerns regarding the current administration')

            #Send the actual content of the message
            stringNum = str(random.randint(0,1))
            myFile = "genMessage"+stringNum+".txt"

            #Parse actual file & load message into variable

            contents = self.replace_word(myFile, "King")
            message_box = driver.find_element_by_xpath('//*[@id="input-F6C4EB2B-E12A-A1F7-6979-6D62DF9DA6AE"]')
            message_box.send_keys(unicode(contents, errors = 'ignore'))

            #Submit information
            #submit_button = driver.find_element_by_xpath('//*[@id="EF6E3EF5-C2D4-9C1C-1649-BD1D51840BC3"]/div[6]/div/input')
            #submit_button.click()


            time.sleep(3600)





collinsForm = AutomateForm('https://www.collins.senate.gov/contact').autoFillCollins()
#kingForm = AutomateForm('https://www.king.senate.gov/contact').autoFillKing()
