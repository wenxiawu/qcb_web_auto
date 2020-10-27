# from common import base_search  #导入函数文件
# from test_data import test_d  #导入测试数据 文件
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)

import time
def login_page(username,password,driver):        #形参  --参数化 --提高代码的复用率
    driver.find_element_by_xpath("//input[@id = 'username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id = 'password']").send_keys(password)
    driver.find_element_by_xpath("//button[contains(text(), '立即登录')]").click()

def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

def seach_key(url,username,password,s_key,driver):
    open_url(driver, url)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    p_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    f_id = p_id + "-frame"
    driver.switch_to.frame(f_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    # obj = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div")
    # if len(obj) == 0:
    #     num = 0
    # else:
    #     num = obj.text
    try:
        num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text
    except:
        num = 0
    return num

