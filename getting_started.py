from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse

# contain username, password for login
username = None
password = None
# TODO: it should come from arg
target_url = "https://dashboard.getalice.ai/" 

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--username')
   parser.add_argument('--password')
   args = parser.parse_args()
   username = args.username
   password = args.password 

if username is None or password is None:
  print('---- please provide login credential for sign-in')
  print('usage: python filename --usernam username --password password')
  exit()
driver = webdriver.Firefox()
assert 'ALICE' in driver.title
driver.get(target_url)
driver.find_element_by_id("userName").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

login_btn = driver.find_element_by_class_name('login-button-round')
driver.execute_script("arguments[0].click();", login_btn)
