from selenium import webdriver
import time


def get_robot_num ( driver ):
    elem_parent = 'robotList'
    elem_chlild = 'robotList_li'
    elem_loc = driver.find_element_by_class_name (elem_parent).find_elements_by_class_name (elem_chlild)
    robot_num = len (elem_loc)
    print ('robot_num=' , robot_num)
    return robot_num


def get_robot_name ( driver ):
    driver = webdriver.Chrome ()
    robot_num = get_robot_num (driver)
    elem_ul = 'robotList'
    elem_li = 'robotList_li'
    robot_name_elem = 'robot_name'
    robot_names = []
    for index in robot_num:
        robot_name_loc = driver.find_element_by_class_name (elem_ul).find_elements_by_class_name (elem_li)[
            index].find_element_by_class_name (robot_name_elem)
        robot_name = robot_name_loc.text
        robot_names.append (robot_name)
    print ('robot_names=' , robot_names)
    return robot_names

#
# def click_robot ( driver , robot_name ):
#     for robot_name in get_robot_name(driver):



if __name__ == '__main__':
    driver = webdriver.Chrome ()
    driver.get ('http://sunland2.exp/?#/robotList')
    time.sleep (3)
    get_robot_num (driver)
