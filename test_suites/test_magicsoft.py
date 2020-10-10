import unittest
from framework.logger import Logger
from selenium.common import exceptions
from framework.browser_engine import BrowserEngine
from pageobjects.HomepageMS import HomePage
logger = Logger(logger="BasePage").getlog()

class Test_GetPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        # f = open(r'D:\SeleniumAutomatioTutorials\automation_framework_demo-master\data\user_data.csv','r+')
        try:
            homepage = HomePage(self.driver)
            homepage.get_windows_img()
            homepage.get_page_title()
            # homepage.click_contact()
            homepage.type_username('Admin')
            homepage.type_password('admin123')
            try:
                homepage.click_login_button()
            except:
                homepage.sleep(30)

            try:
                homepage.get_page_title()
            except:
                homepage.get_page_title()
            homepage.get_windows_img()
            try:
                homepage.click_dd_logout_link()
            except exceptions.StaleElementReferenceException as e:
                homepage.click_dd_logout_link()
                print(e)

            try:
                homepage.click_logout_link()
            except:
                pass
                # homepage.click_logout_link()
            homepage.sleep(30)
            try:
                homepage.get_page_title()
            except:
                homepage.get_page_title()
            homepage.get_windows_img()
            homepage.sleep(20)
            logger.info("The Test case Passed")
        except Exception as e:
            logger.error("The Test case failed : "+ str(e))
            print(e)

if __name__ == '__main__':
    unittest.main()
