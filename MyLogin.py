class Chrome:

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("file:///C:/Users/Abhijit/Desktop/Selenium/login.html")

driver.f_element_by_id("123").send_keys("Admin")
driver.find_element_by_id("4321").send_keys("pswrd")

#driver.find_element_by_name("ln").click()

driver.close()

