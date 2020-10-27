
'''
xpath:
1.绝对路径（定位到元素，右击-Copy-Copy XPath）：/html/body/div/div/div[1]/a/b    ----根节点
    具有顺序性、继承关系，一旦开发修改----就会失效，不稳定，不安全
    ---面试不提，工作里不用
2.相对路径：只靠自己的特征定位    //开头  ---- 加上我关心节点的标签名
   ---标签名+属性 = //标签名[@属性名 = 属性值]
   ---//input[@id = "username"]    ----xpath表达式
注意：Xpath搜索框--确定xpath表达式是否能唯一定位到元素：F12-Elements-Ctrl+F

对页面进行对应的操作：
1）点击：click
2）传值：send_keys
3）获取页面文本：text
4）获取属性
'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)   #隐式等待，默认等待10s  ==== 最多等待10s，提前加载好，不继续等待
driver.get("http://erp.lemfix.com/")
driver.maximize_window()
# 找到这个元素的位置之后获取文本信息
page_text = driver.find_element_by_xpath("//div[@class='login-logo']//b").text
page_title = driver.title
print(page_title)
if page_text == "柠檬ERP":
    print("这个页面的标题是{}".format(page_text))
else:
    print("这条测试用例不通过")
driver.find_element_by_xpath("//input[@id = 'username']").send_keys("test123")
driver.find_element_by_xpath("//input[@id = 'password']").send_keys("123456")
driver.find_element_by_xpath("//button[contains(text(), '立即登录')]").click()

'''
但凡是切换了页面，页面没有加载完，元素不显示  ====  最好加个等待
三种等待方式：
1.强制等待：time.sleep()  ====  没有完成等待时间，不往下执行
2.智能等待：
    隐式等待：可以设置一个等待时间，在这个等待时间没有结束之前，不继续等待了，继续执行下面的代码---灵活
    注意：一个session 里面只执行一次 ----- 在初始化的时候添加
    显式等待：expected_condition   ===  Python班级会讲，目前不需要掌握
'''
# 第5条用例
# time.sleep(5)  #强制等待5s
login_user = driver.find_element_by_xpath("//p[text()='测试用户']").text  #获取登录用户名
if login_user == "测试用户":
    print("这个登录的用户是：{}".format(login_user))
else:
    print("这条测试用例不通过")
#点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()

'''
1.识别是否有子页面的方式：页面层级路径里出现iframe：就需要去切换iframe才可以进行元素的定位
2.怎么去切换：
    1）找到这个iframe元素
    2）通过元素定位（xpath）来切换iframe
    3）iframe下标：从0开始    html-页面 = 0，第一个宝宝-1，第二个宝宝-2
'''
#通过找到这个元素 --- 获取id属性
p_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
f_id = p_id + "-frame"
# #1.通过id进行的iframe切换
# driver.switch_to.frame(f_id)

#2.通过元素定位（xpath）来切换iframe  --- 扩展
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{0}']".format(f_id)))
#3.通过iframe的下标  来切换
driver.switch_to.frame(1)
#搜索框输入314
driver.find_element_by_id("searchNumber").send_keys("314")
#点击搜索按钮
driver.find_element_by_id("searchBtn").click()
time.sleep(1)
#找到单据编号
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']/td[@field='number']/div").text
if '314' in num:
    print("搜索的结果是正确的！")
else:
    print("用例测试不通过")


