from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")
time.sleep(5)

#//*[@id="email"]
username = browser.find_element_by_xpath("//*[@id='email']")
passver = browser.find_element_by_name("pass")
username.send_keys(" (write your mail for faceebook) ")
passver.send_keys("(write your password for facebook) ")
time.sleep(1)

#//*[@id="u_0_b"]
login = browser.find_element_by_xpath("//*[@id='u_0_b']")
login.click()
time.sleep(10)
browser.quit()
