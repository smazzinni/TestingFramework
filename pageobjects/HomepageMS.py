import unittest

from framework.base_page import BasePage

class HomePage(BasePage):
    # contact = 'xpath=>/html/body/div[2]/div[1]/div[1]/div[3]/div/div/a'
    user = 'xpath=>//*[@id="txtUsername"]'
    passwd = 'xpath=>//*[@id="txtPassword"]'
    login_button = 'xpath=>//*[@id="btnLogin"]'
    dd_logout = 'id=>welcome'
    # logout_link = 'link_text=>Logout'
    logout_link = 'selector_selector=>#welcome-menu > ul:nth-child(1) > li:nth-child(2) > a'
    def click_contact(self):
        self.click(self.contact)

    def type_username(self, text):
        self.type(self.user, text)

    def type_password(self, text):
        self.type(self.passwd, text)

    def click_login_button(self):
        self.click(self.login_button)

    def click_dd_logout_link(self):
        self.click(self.dd_logout)

    def click_logout_link(self):
        self.click(self.logout_link)
