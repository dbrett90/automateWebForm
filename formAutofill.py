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

class AutomateForm(object):

    def __init__(self, url):
        self.url = url


    def autoFillCollins(self):
        #Send Ten emails, one each hour. Values can be adjusted to annoy representatives if needed.
        for x in range(10):
            #Open a new browser w/ Collins URL
            driver = webdriver.Chrome()
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
            myFile = "collinsEmails"+stringNum+".txt"

            #Parse actual file & load message into variable

            in_file = open("messageTemplates/"+myFile, "rt")
            contents = in_file.read()
            in_file.close()
            message_box = driver.find_element_by_xpath('//*[@id="edit-submitted-please-write-your-message"]')
            message_box.send_keys(unicode(contents, errors = 'ignore'))

            #pause for an hour
            time.sleep(3600)


        #Submit all information - uncomment this line in order to submit information from files
        #submit_button = driver.find_element_by_xpath('//*[@id="webform-client-form-9020"]/div/div[16]/input')
        #submit_button.click()

form = AutomateForm('https://www.collins.senate.gov/contact').autoFillCollins()
