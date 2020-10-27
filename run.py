
from common import base_search  #导入函数文件
from test_data import test_d  #导入测试数据 文件
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
#调用函数
url = test_d.url["url"]
user = test_d.login_data[0]["username"]
password = test_d.login_data[1]["password"]
s_key = test_d.s_key["s_key"]
result = base_search.seach_key(driver=driver,url=url,username=user,password=password,s_key=s_key)
if s_key in result:
    print("搜索结果是正确的")
else:
    print("用例测试不通过")

