# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):


        # logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)


        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/automation_framework_demo-master/Logs/'  # log path
        # log_path = os.path.dirname(os.path.abspath('.')) + '/automation_framework_demo-master/logs/'
        # log_path = os.path.dirname(os.path.abspath('')) + '/automation_framework_demo/logs/'
        log_name = log_path + rq + '.log'

        print(log_name)
        # with open(log_name, "w+") as f:
        #     pass
        try:
            f = open(log_name,'w+')
        except Exception as e :
            print(e)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)


        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)


        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # logger handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
