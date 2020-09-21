from selenium import webdriver

email = input("your gmail ")
password = input("your password ")

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.gmail.com")

driver.find_element_by_name("identifier").send_keys(email)

driver.find_element_by_class_name("VfPpkd-RLmnJb").click()

driver.implicitly_wait(10)

driver.find_element_by_name('password').send_keys(password)

driver.implicitly_wait(4)

driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()