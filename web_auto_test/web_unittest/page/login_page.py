class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def login(self):
        self.driver.find_element_by_xpath().send_keys()
