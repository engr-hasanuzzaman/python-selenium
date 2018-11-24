import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginToAlice(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.url = 'https://dashboard.getalice.ai/'
    credits_file = open("credential.txt", "r")
    lines = credits_file.readlines()
    credits_file.close()
    self.username = lines[0]
    self.password = lines[1]

  def test_login(self):
    driver = self.driver
    driver.get(self.url)
    assert 'ALICE' in driver.title
    driver.find_element_by_id("userName").send_keys(self.username)
    driver.find_element_by_id("password").send_keys(self.password)

    login_btn = driver.find_element_by_class_name('login-button-round')
    driver.execute_script("arguments[0].click();", login_btn)

  def read_credential(self):
    credits_file = open("credential.txt", "r")
    lines = credits_file.readlines()
    credits_file.close()
    self.username = lines[0]
    self.password = lines[1]

  def tearDown(self):
    self.driver.close()

# print("current file name is %s, name %s"%(__file__, __name__))
if __name__ == "__main__":
    unittest.main()