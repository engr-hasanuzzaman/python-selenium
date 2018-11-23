from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get ("https://dashboard.getalice.ai/")
driver.find_element_by_id("userName").send_keys("test.misfit")
driver.find_element_by_id("password").send_keys('qwerty123456')

login_btn = driver.find_element_by_class_name('login-button-round')
driver.execute_script("arguments[0].click();", login_btn)
