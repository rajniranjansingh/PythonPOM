class LoginPage():
    username_id = "Email"
    password_id = "Password"
    loginButton_xpath = "//input[@type='submit']"
    logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self,driver):   # This is constructor of the class. This will get invoked whenver we will access this class and will initiate the driver
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.loginButton_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_xpath ).click()