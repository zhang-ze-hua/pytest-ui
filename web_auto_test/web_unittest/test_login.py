import unittest
from selenium import webdriver
from ddt import ddt, data
from web_unittest.page.login_page import LoginPage
from web_unittest.page.index_page import IndexPage


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page_driver = LoginPage(self.driver)
        self.index_page_driver = IndexPage(self.driver)

    @data()
    def test_login_pass(self):
        pass

    @data()
    def test_login_pass(self):
        pass

    def tearDown(self):
        self.driver.quit()
