from selenium import webdriver
import unittest
from common.common_info import *
from .qa_robot_page import QaRobotPage
from common.mysql_util import MysqlUtil
import time
import os
import HTMLTestRunner


class QaRobotSpec (unittest.TestCase):

    def setUp ( self ):
        self.driver = webdriver.Chrome ()
        self.driver.implicitly_wait (30)
        self.driver.maximize_window ()
        self.driver.get (base_url)
        self.qaRobotPage = QaRobotPage (self.driver)
        self.mysqlUtil = MysqlUtil ()

    def tearDown ( self ):
        self.driver.quit ()

    def test_one_qa ( self ):
        question = '你好'
        answer = '没有可用的答案！'
        self.qaRobotPage.open_dialog ()
        self.qaRobotPage.select_robot ()
        self.qaRobotPage.send_question (question)
        robot_answer = self.qaRobotPage.get_answer ()
        self.assertEqual (robot_answer , answer)

    # def test_all_qa ( self ):
    #     sql = 'select question from ai_question'
    #     all_question = self.mysqlUtil.fetchall (sql)
    #     self.qaRobotPage.open_dialog ()
    #     for question in all_question:
    #         self.qaRobotPage.send_question (question)
    #         robot_answer = self.qaRobotPage.get_answer ()
    #         self.assertTrue (robot_answer)


if __name__ == '__main__':
    unittest.main ()

    # testSuite = unittest.TestSuite ()
    # testSuite.addTest (QaRobotSpec ('test_one_qa'))
    #
    # # -------------------------------------------------------------------------------------------------------------------------
    # now = time.strftime ('%Y%m%d-%H:%M%S')
    # file_name = os.path.abspath (os.path.dirname (__file__) + '/../../../test_reports/') + now + '_result.html'
    # testReport = open (file_name , 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner (stream=testReport , title='智能机器人UI测试报告' , description='测试用例执行情况')
    # runner.run (testSuite)
