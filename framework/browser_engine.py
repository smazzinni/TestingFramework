

import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))
    # chrome_driver_path = dir + '/tools/chromedriver.exe'
    # ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/automation_framework_demo-master/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(IEDriverManager().install())
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(60)
        logger.info("Set implicitly wait 60 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()




