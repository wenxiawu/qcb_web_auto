
'''
web自动化：
代码            翻译（中间人）       浏览器
Python    -----> 浏览器驱动  ------>  Chrome
selenium：Python的工具，包括3个部分 ---了解
1）ide：录制脚本---用得少
2）webdriver：--提供对网页的各种操作 + 结合语言使用  --  Python 、java--重点
3）grid：分布式 ---用得少
'''
# import selenium #工具里所有的内容都导入，一般不推荐这样使用
from selenium import webdriver  #从selenium工具中导入webdriver库
import time       # 导入time这个模块  ---- python自带的
driver = webdriver.Chrome()   #选择chrome这个浏览器，初始化driver == 可用浏览器进行沟通  建立会话 = session
# 1.打开一个网址
# driver.get("http://baidu.com/")  #打开一个网址
# 2.浏览器窗口最大化
# driver.maximize_window()
# # 3.打开新页面
# time.sleep(2)   # 等待，默认秒
# driver.get("http://erp.lemfix.com/")
# # 4.向前、退后、刷新
# time.sleep(2)
# driver.back()    #退回到上一个页面
# time.sleep(2)
# driver.forward()   # 前进到下一个页面
# time.sleep(2)
# driver.refresh()   # 刷新页面
# # 5.退出
# driver.quit()  #关闭驱动   session关闭
# driver.close()  #关闭当前窗口，不会退出会话

#以上是浏览器的常规操作，给常规的操作---要怎么实现呢？======元素定位
'''
基础知识：web页面 ====HTML+CSS+JavaScript   ----扩展，了解
html：标签语言<标签名>值</标签名>  ==== 呈现页面内容
CSS：页面布局设置，字体颜色，字体大小样式
JS：依据不同效果

元素的特征：根据页面设计规则，有些特征是唯一  === 开发遵循了这个规则
id：类比身份证号码 === 仅限于当前页面  比如  username  password
注意：如果id  不是固定的话，就不能使用来定位

对页面进行对应的操作：
1）点击：click
2）传值：send_keys
'''
driver.get("http://erp.lemfix.com/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("test123")  #找到了有username这id的元素---点击、输入内容
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

