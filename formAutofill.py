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


#Google Drive Link = https://docs.google.com/forms/d/e/1FAIpQLSdrqmqAdP_X5TzjNYlGr5Zo6sY_Q-rB6ATxa5Htd1QqZMYSQg/viewform?usp=sf_link, pwd = /Users/dbrett/Library/Python/2.7/lib/python/site-packages

def autoFillGoogle(url):
    #opening Chrome to access web broswer
    driver = webdriver.Chrome()
    driver.get(url)


    #Define data that will be auto-submitted with form
    first_name = 'Dan'
    last_name = 'Brett'
    address = '15 Loveitt Street'
    city = 'South Portland'
    state = 'Maine'
    zip_code = '04106'
    email = 'dbrett14@gmail.com'
    message = 'Running every sixty seconds'

    #Enter actual information into appropriate boxes using unique xpaths
    first_name_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input')
    first_name_box.click()
    first_name_box.send_keys(first_name)

    last_name_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/input')
    last_name_box.click()
    last_name_box.send_keys(last_name)

    address_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/div[1]/div/div[1]/input')
    address_box.click()
    address_box.send_keys(address)

    city_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div[2]/div/div[1]/div/div[1]/input')
    city_box.click()
    city_box.send_keys(city)

    #Tough area with the dropdown
    #state_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div[2]/div[1]/div[1]/div[3]/content')
    #state_box = driver.find_element_by_class_name("quantumWizMenuPaperselectContent").click()
    #options = driver.find_element_by_class_name("exportSelectPopup")


    zip_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[8]/div[2]/div/div[1]/div/div[1]/input')
    zip_box.click()
    zip_box.send_keys(zip_code)

    email_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[11]/div[2]/div/div[1]/div/div[1]/input')
    email_box.click()
    email_box.send_keys(email)

    message_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[13]/div[2]/div[1]/div[2]/textarea')
    message_box.click()
    message_box.send_keys(message)

    #Submit the above information
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span').click()


#URL for Susan Collins: https://www.collins.senate.gov/contact
def autoFillCollins(url):
    #Open a new browser w/ Collins URL
    driver = webdriver.Chrome()
    driver.get(url)

    #Upload the normal fields
    xpath_dict = {'//*[@id="edit-submitted-first-name"]': 'Dan', '//*[@id="edit-submitted-last-name"]':'Brett', '//*[@id="edit-submitted-address-1"]':'15 Loveitt Street', '//*[@id="edit-submitted-city-town"]':'South Portland', '//*[@id="edit-submitted-zip-code"]':'04106', '//*[@id="edit-submitted-e-mail"]': 'dbrett14@gmail.com'}
    for key in xpath_dict:
        box = driver.find_element_by_xpath(key)
        box.send_keys(xpath_dict[key])

    #Fill in radio buttons (fuck subscribing to some shit)
    driver.find_elements_by_css_selector("input[type = 'radio'][value = 'No']")[1].click()

    #Fill in State dropdown
    mySelect = Select(driver.find_element_by_id('edit-submitted-state'))
    mySelect.select_by_visible_text('Maine')

    #Fill in Message from message bank by randomly selecting which file/message to send
    stringNum = str(random.randint(0,1))
    myFile = "collinsEmails"+stringNum+".txt"

    #Parse actual file & load message into variable

    in_file = open(myFile, "rt")
    contents = in_file.read()
    in_file.close()
    print(contents)

    message_box = driver.find_element_by_xpath('//*[@id="edit-submitted-please-write-your-message"]')
    message_box.send_keys(unicode(contents, errors = 'ignore'))





#Schedule the program to run every 10 minutes so as to annoy your representative until they respond
def main_method():
    for x in range(10):
        #autoFillGoogle('https://docs.google.com/forms/d/e/1FAIpQLSdrqmqAdP_X5TzjNYlGr5Zo6sY_Q-rB6ATxa5Htd1QqZMYSQg/viewform?usp=sf_link')
        autoFillCollins('https://www.collins.senate.gov/contact')
        time.sleep(3600)

main_method()
