from common.common_info import *
from .qa_robot_elem import *


class QaRobotPage:
    def __init__ ( self , driver ):
        self.driver = driver
        self.url = base_url

    def open_dialog ( self ):
        robotImg_loc = self.driver.find_element_by_id (robotImg_id)
        return robotImg_loc.click ()

    def select_robot ( self ):
        robot_loc = self.driver.find_element_by_xpath (teacher_xpath)
        return robot_loc.click ()

    def send_question ( self , question ):
        dialogInput_loc = self.driver.find_element_by_xpath (dialogInput_xpath)
        dialogInput_loc.click ()
        dialogInput_loc.send_keys (question)

    def get_answer ( self ):
        robotAnswer_loc = self.driver.find_elements_by_class_name (robotAnswer_class_name)
        answer_len = len (robotAnswer_loc)
        new_answer_loc = robotAnswer_loc[answer_len].find_element_by_tag_name ('span')
        new_answer = new_answer_loc.text
        return new_answer
