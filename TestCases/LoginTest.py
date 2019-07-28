import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
import time
sys.path.append("/Users/rajniranjansingh/PycharmProjects/POMBased/Pages/LoginPage.py")

from Pages.LoginPage import LoginPage

class test_login(unittest.TestCase):

    baseURL = "http://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome("/Users/rajniranjansingh/PycharmProjects/POMBased/Drivers/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Home Page Title doesn't match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__  == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/rajniranjansingh/PycharmProjects/POMBased/Reports"))