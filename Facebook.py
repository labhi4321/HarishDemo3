from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.facebook.com/")

driver.implicitly_wait(10)

driver.find_element_by_xpath('//input[@id="email"]').send_keys("Abhijit")
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("admin")
driver.find_element_by_xpath('//input[@name="firstname"]').send_keys("Abhijit")
driver.find_element_by_xpath('//input[@name="lastname"]').send_keys("Dey")


