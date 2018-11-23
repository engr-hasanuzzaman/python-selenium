# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import argparse
# driver = webdriver.Firefox()
# driver.get ("https://dashboard.getalice.ai/")
# driver.find_element_by_id("userName").send_keys("test.misfit")
# driver.find_element_by_id("password").send_keys('qwerty123456')

# login_btn = driver.find_element_by_class_name('login-button-round')
# driver.execute_script("arguments[0].click();", login_btn)
if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--name')
   parser.add_argument('--age')
   args = parser.parse_args()

   print(args.name)
   print(args.age)

   my_dict = {'arg1': args.name, 'arg2': args.age }
   print(my_dict)