from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import configparser

capabilities = {'chromeOptions':{
			'useAutomationExtension':False,
	}
}

try:
	driver = webdriver.Chrome(desired_capabilities=capabilities)
	driver.implicitly_wait(30)

	config = configparser.ConfigParser()
	config.read("config.ini")
	dev = config["DEVELOPER"]
	username = dev.get("USER")
	password = dev.get("PASS")

	config.read("config.ini")
	dev = config["DEV"]
	username2 = dev.get("USER")
	password2 = dev.get("PASS")


	driver.get('https://tools.standardbank.co.za/jira/login.jsp')
	driver.find_element_by_id('txtUserName').send_keys(username)
	driver.find_element_by_id('txtPassword').send_keys(password,Keys.TAB,Keys.TAB,Keys.ENTER)

	driver.get('http://clientfirstbooking.standardbank.co.za/Login/login.aspx')
	driver.find_element_by_id('txtUserName').send_keys(username2)
	driver.find_element_by_id('txtPassword').send_keys(password2,Keys.TAB,Keys.ENTER)

except BaseException as e:
	print("Error: ", e )