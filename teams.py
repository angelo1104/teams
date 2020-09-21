from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=3b4b794a-ec86-4706-a089-6168db7e6cbc&&client-request-id=970bbab7-b54f-423f-b08a-95f47b51ede8&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=17e9bbad-3065-4cac-94cc-656eb9325b73&domain_hint=')

driver.implicitly_wait(20)

driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]').send_keys('madhav4812.risp@indirapuramschool.onmicrosoft.com')

driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div').click()

driver.implicitly_wait(10)

driver.find_element_by_id('i0118').send_keys('Keepoutjp101')

driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div').click()

driver.implicitly_wait(10)

driver.find_element_by_xpath('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]').click()

driver.implicitly_wait(300)

driver.find_element_by_xpath('/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a').click()

driver.implicitly_wait(600)

time.sleep(10)

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/app-bar/nav/ul/li[5]/button').click()
