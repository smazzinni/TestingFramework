
# import HtmlTestRunner
from framework import HTMLTestRunner
import os
import unittest
import time
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()

report_path = os.path.dirname(os.path.abspath('')) + '/automation_framework_demo-master/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


HtmlFile = report_path + now + "HTMLReport.html"
try:
    fp = open(HtmlFile, "w+")
except FileNotFoundError as e:
    logger.error("File not found error  : " + e)

# Testsuite
suite = unittest.TestLoader().discover("")

if __name__ =='__main__':
    # with open(HtmlFile, 'w+') as fp:
    # HTMLTestRunner
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Test Suit", description=u"Test Suite HTML Report")
    runner.run(suite)



