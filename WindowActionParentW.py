from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")

driver.get("https://phptravels.com/")
driver.implicitly_wait(10)
driver.maximize_window()
current_win_id=driver.current_window_handle
#print(win_id)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[8]/a/span').click()
mul_win_id=driver.window_handles
#print(mul_win_id)
#print(type(mul_win_id))

#for loop for handling multiple Windows
for id in mul_win_id:
    if(current_win_id !=id):
        driver.switch_to.window(id)
        driver.find_element_by_id("inputEmail").send_keys("Hi There ")
        print("Test case passed:It entered data on Child Window ")

time.sleep(5)
driver.switch_to.window(mul_win_id[0])
driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[1]/span').click()
print("Clicked on Demo on Parent Window ")

driver.quit()


