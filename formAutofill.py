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
    
    def mr_or_mrs(self, name):
        if name == "Sofia" or name == "Maria":
            return "Ms."
        if name == "Orysia":
            return "Mrs."
        else:
            return "Mr."
    
    def last_name(self, first_name):
        if first_name == 'DJ':
            return "Jayachandran"
        else:
            return "Soroka"




    def autoFillCollins(self):
        #Send Ten emails, one each hour. Values can be adjusted to annoy representatives if needed.
        for x in range(10):
            #Open a new browser w/ Collins URL
            driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
            driver.get(self.url)

            #Upload the normal fields
            xpath_dict = {'//*[@id="edit-submitted-first-name"]': 'Dan', '//*[@id="edit-submitted-last-name"]':'Brett', '//*[@id="edit-submitted-address-1"]':'6 Kelly Lane', '//*[@id="edit-submitted-city-town"]':'Scarborough', '//*[@id="edit-submitted-zip-code"]':'04074', '//*[@id="edit-submitted-e-mail"]': 'dbrett14@gmail.com'}
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



            #Submit all information - uncomment this line in order to submit information from files
            submit_button = driver.find_element_by_xpath('//*[@id="webform-client-form-9020"]/div/div[16]/input')
            submit_button.click()
            time.sleep(3600)
        #pause for an hour

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
            submit_button = driver.find_element_by_xpath('//*[@id="EF6E3EF5-C2D4-9C1C-1649-BD1D51840BC3"]/div[6]/div/input')
            submit_button.click()


            time.sleep(3600)
    
    def autofillBooker(self):
        #Do 12 times so there is a good chance that all are selected
        
        driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
        driver.get(self.url)

        #upload all required fields that have short answer

        #Names list
        names_list = ['Sofia', 'John', 'Paul', 'Maria', 'Orysia', 'Eugene']
        rand_num = random.randint(0, len(names_list)-1)
        #Find Xpath of the first name
        first_name_xpath = driver.find_element_by_xpath('//*[@id="firstName"]')
        first_name_xpath.send_keys(names_list[rand_num])
        submit_button = driver.find_element_by_xpath('//*[@id="initialSubmit"]')
        submit_button.click()
        #Wait for dropdown to load with sleep function
        time.sleep(3)

        mySelect = Select(driver.find_element_by_id('topicsSelect'))
        mySelect.select_by_visible_text('Foreign Relations')
        #wait for next page
        time.sleep(2)

        #Write function to choose Mr. or Mrs. and select
        prefix = self.mr_or_mrs(names_list[rand_num])
        #prefix = self.mr_or_mrs(names_list[rand_num])
        nextSelect = Select(driver.find_element_by_id('input-2AA38DC3-BC1F-9589-8FDC-7341685E655F'))
        nextSelect.select_by_visible_text(prefix)

        #Institute xpath_dict to loop through and send keys
        xpath_dict = {'//*[@id="input-2AB4270E-EBD3-21C4-9AD3-CA2D60AFF043"]':'Soroka', '//*[@id="input-2AF31262-E7B8-AC75-3CAA-EF2A847439DD"]':'77 Mounthaven Drive', '//*[@id="input-2AF312C2-B40C-D3C3-05F6-ECB0009872D9"]':'Livingston' , '//*[@id="input-2AF31332-B8C6-5B56-4258-713E6C23C0C4"]': '07039', '//*[@id="email"]': 'sofi.1018@gmail.com', '//*[@id="input-2B043CF1-FA12-237B-D8AD-54FE21726597"]': 'sofi.1018@gmail.com', '//*[@id="input-2AFF692A-04A2-EBBA-5021-824732C5E367"]': '9739089209', '//*[@id="input-2B0D4D7C-FE79-F9BE-4491-935B036375CC"]': 'Supporting Ukraine against Russian Incursion'}
        for key in xpath_dict:
            box = driver.find_element_by_xpath(key)
            box.send_keys(xpath_dict[key])
        
        stringNum = str(random.randint(0,1))
        myFile = "genMessage"+stringNum+".txt"

        #Parse actual file & load message into variable

        contents = self.replace_word(myFile, "Booker")
        message_box = driver.find_element_by_xpath('//*[@id="input-2B10C291-92F3-C0D2-11A5-6B0CC8EA12C0"]')
        message_box.send_keys(unicode(contents, errors = 'ignore'))

        #Check the radio buttons
        driver.find_element_by_xpath('//*[@id="input-2B628374-ED07-D0C7-FF9D-B7D166244267"]/div[1]/div/label').click()
        driver.find_element_by_xpath('//*[@id="newsletteraction"]/div[2]/div/label').click()

        #submit button
        driver.find_element_by_xpath('//*[@id="2A9B34FE-A96D-4B35-5C05-91EF928C204A"]/div[15]/div/button').click()

    
    def autofillMenendez(self):
        driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
        driver.get(self.url)

        #upload all required fields that have short answer

        #Names list
        names_list = ['Sofia', 'John', 'Paul', 'Maria', 'Orysia', 'Eugene']
        rand_num = random.randint(0, len(names_list)-1)
        #Randomly select a first name from the list
        rand_name = names_list[rand_num]
        #Assign gender accordingly
        prefix = self.mr_or_mrs(rand_name)
        nextSelect = Select(driver.find_element_by_id('input-EAC8D6B7-F9EE-BEBF-A75A-C454ACF0F430'))
        nextSelect.select_by_visible_text(prefix)

        #Hash with all remaining fields you need
        xpath_dict = {'//*[@id="input-EAC8D70B-E94B-29C2-9DAD-687D64BAF101"]':rand_name, '//*[@id="input-EAC8D7AB-B9FB-5DEB-AAD0-25C23587B1C6"]':'Soroka', '//*[@id="input-EACEAAD2-DDC8-BEDB-3215-33ED0B87C3EB"]':'77 Mounthaven Drive', '//*[@id="input-EACEAB65-9055-42AD-471F-DA6441629542"]':'Livingston' , '//*[@id="input-EACEABFB-AA5F-BB82-BB45-02ED27D08472"]': '07039', '//*[@id="email"]': 'sofi.1018@gmail.com', '//*[@id="input-EADC3F6B-BBD7-18B7-580E-2BC21F585E17"]': 'sofi.1018@gmail.com', '//*[@id="input-EAD2D9EC-F044-C4D6-489C-84E3A7006FE9"]': '9739089209'}
        for key in xpath_dict:
            box = driver.find_element_by_xpath(key)
            box.send_keys(xpath_dict[key])
        
        #Select the topic
        topicSelect = Select(driver.find_element_by_id('input-EAE6B071-04DF-161B-6A14-46D3754DCB90'))
        topicSelect.select_by_visible_text('Foreign Relations')

        #Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Send Message
        stringNum = str(random.randint(0,1))
        myFile = "genMessage"+stringNum+".txt"

        contents = self.replace_word(myFile, "Menendez")
        message_box = driver.find_element_by_xpath('//*[@id="input-EAEF05AF-98D2-6504-C198-007A3E8A4323"]')
        message_box.send_keys(unicode(contents, errors = 'ignore'))

        #Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #Get Response
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="EAA4FD22-FFDE-AFE5-6AFC-D95CF4F154E7"]/fieldset[2]/div[5]/label').click()
        #Submit form
        driver.find_element_by_xpath('//*[@id="EAA4FD22-FFDE-AFE5-6AFC-D95CF4F154E7"]/div[2]/div/button').click()

    
    def autofillGillibrand(self):
        driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
        driver.get(self.url)

        #upload all required fields that have short answer
        #Names list - NY residents specifically
        names_list = ['Sofia', 'Maria', 'DJ']
        rand_num = random.randint(0, len(names_list)-1)
        #Randomly select a first name from the list
        rand_name = names_list[rand_num]
        #Get prefixes and last names for residents
        prefix = self.mr_or_mrs(rand_name)
        last_name = self.last_name(rand_name)
        time.sleep(3)

        #Pass in prefix
        nextSelect = Select(driver.find_element_by_id('input-A5AD3428-5056-A066-6005-7CBE3BA4A089'))
        nextSelect.select_by_visible_text(prefix)

        #Use xpath_hash to pass in remaining key variables
        xpath_dict = {'//*[@id="input-A5AD3024-5056-A066-60BD-27089EC367B6"]':rand_name, '//*[@id="input-A5AD2D97-5056-A066-609C-2BE7421DED54"]':last_name, '//*[@id="input-A5AD3726-5056-A066-6040-8733FE9F1C74"]':'141 2nd Ave', '//*[@id="input-A5AD3598-5056-A066-602E-1929FB800695"]':'New York City' , '//*[@id="input-A5AD3404-5056-A066-6010-890AB748A186"]': '10003', '//*[@id="email"]': 'sofi.1018@gmail.com', '//*[@id="input-A5AD3157-5056-A066-6044-877D1CC4A989"]': '9739089209'}
        for key in xpath_dict:
            box = driver.find_element_by_xpath(key)
            box.send_keys(xpath_dict[key])
        
        #Select Radio button about foreign policy
        #driver.find_element_by_xpath('//*[@id="issue-12"]').click()
        message_topic_select = Select(driver.find_element_by_xpath('//*[@id="contactdropdown"]'))
        message_topic_select.select_by_visible_text('Foreign Relations/International Affairs')

        #Send message
        #Send Message
        stringNum = str(random.randint(0,1))
        myFile = "genMessage"+stringNum+".txt"

        contents = self.replace_word(myFile, "Gillibrand")
        message_box = driver.find_element_by_xpath('//*[@id="input-A5AD3307-5056-A066-6029-D7EBFF775924"]')
        message_box.send_keys(unicode(contents, errors = 'ignore'))

        #Submit
        driver.find_element_by_xpath('//*[@id="A5AD2BDE-5056-A066-60D8-0ADE8864FC1C"]/div[2]/div/input').click()
    
    def autofillSchumer(self):
        driver = webdriver.Chrome(executable_path="/home/daniel/chromedriver")
        driver.get(self.url)

        #upload all required fields that have short answer

        #Names list - NY residents specifically
        names_list = ['Sofia', 'Maria', 'DJ']
        rand_num = random.randint(0, len(names_list)-1)
        #Randomly select a first name from the list
        rand_name = names_list[rand_num]
        #Get prefixes and last names for residents
        prefix = self.mr_or_mrs(rand_name)
        last_name = self.last_name(rand_name)

        #Choose first option
        mySelect = Select(driver.find_element_by_xpath('//*[@id="actions"]'))
        mySelect.select_by_visible_text('Share your opinion or comments on bills or other issues')
        time.sleep(2)
        #pass in prefix
        prefixSelect = Select(driver.find_element_by_xpath('//*[@id="salutation"]'))
        prefixSelect.select_by_visible_text(prefix)

        #Pass in xpath info
        xpath_dict = {'//*[@id="fname"]':rand_name, '//*[@id="lname"]':last_name, '//*[@id="mailing_streetAddress1"]':'141 2nd Ave', '//*[@id="mailing_city"]':'New York City' , '//*[@id="mailing_zipCode"]': '10003', '//*[@id="email"]': 'sofi.1018@gmail.com', '//*[@id="verify_email"]': 'sofi.1018@gmail.com', '//*[@id="home_phone_number"]': '9739089209'}
        for key in xpath_dict:
            box = driver.find_element_by_xpath(key)
            box.send_keys(xpath_dict[key])
        

        #select message topic
        message_topic_select = Select(driver.find_element_by_xpath('//*[@id="subject"]'))
        message_topic_select.select_by_visible_text('Foreign Relations')
        #Message subject
        message_subject = driver.find_element_by_xpath('//*[@id="subjecttext"]')
        message_subject.send_keys('Supporting Ukraine against Russian Incursion')
        #Send message
        stringNum = str(random.randint(0,1))
        myFile = "genMessage"+stringNum+".txt"

        contents = self.replace_word(myFile, "Schumer")
        message_box = driver.find_element_by_xpath('//*[@id="message"]')
        message_box.send_keys(unicode(contents, errors = 'ignore'))

        #Submit the message
        driver.find_element_by_xpath('//*[@id="side-search-btn"]').click()
        










#collinsForm = AutomateForm('https://www.collins.senate.gov/contact').autoFillCollins()
#gkingForm = AutomateForm('https://www.king.senate.gov/contact').autoFillKing()
# for x in range(10):
#     JerseyForm1 = AutomateForm('https://www.booker.senate.gov/contact/write-to-cory').autofillBooker()
#     JerseyForm2 = AutomateForm('https://www.menendez.senate.gov/contact/email').autofillMenendez()
#     time.sleep(3543)

for x in range(12):
    gillibrand = AutomateForm('https://www.gillibrand.senate.gov/contact/email-me').autofillGillibrand()
    Schumer = AutomateForm('https://www.schumer.senate.gov/contact/email-chuck').autofillSchumer()
    time.sleep(3543)