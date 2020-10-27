'''
一、变量：存储数据的  ===  保险柜----存储东西
数据类型：int  float  bool  str
变量名：标识符（需要遵守标识符的命名规则,第一节课1，,2，3,4）
5.建议：见名知意
'''
name="彩虹"
'''
6.变量名一定要先声明（定义并赋值），再调用，否则报错
'''
print(name)



'''
二、字符传的操作：
'''
strl="hello world!"
#     01234567891011
'''
1.取值：位置----索引，从0开始，依次加1
'''
print(strl[0])
'''
2.取多个值：  切片：--[开始：结束：步长] ==== 取头不取尾
开始头----可以省略 === 默认从0开始
结束 -----可以省略 === 默认末尾结束
步长 -----  可以省略 === 默认为1
'''
print(strl[2:4:1])
print(strl[:5:2])
print(strl[::2])
'''
3.负数：从右边开始取    -1：最后一个
'''
print(strl[-1])
'''
4.元素个数：len() -- 内置函数：统计元素个数（长度）
'''
print(len(strl))
'''
5.替换字符串里的元素：replace()
'''
strl1=strl.replace("world","Tricy")
print(strl1)
'''
6.检测字符串中是否包含子字符串--找到元素，则返回元素所在位置
'''
# print(strl1.index("g"))  # 如果元素没有找到---会报错，代码终止运行
print(strl1.find("g"))  #如果元素没有找到---不会报错，返回-1
'''
7.用于统计字符串里某个字符出现的次数
'''
print(strl1.count("l"))

'''
三、格式化输出：
1. .format()
（1）占位符：{} -- 传 变量的地方    .format()
（2）.format()  可以默认按顺序传入变量，也可以指定位置传入变量 === 注意：不能混合使用
'''
name="风行"
age=18
hobby="百家讲坛"
print('''---{0}---
name:{0}
age:{1}
hobby:{2}
'''.format(name,age,hobby))
'''
2. %s---字符串==可以匹配所有     %d---整数     %f---小数  ----了解
'''
print('''---%s---
name:%s
age:%d
hobby:%s
'''%(name,name,age,hobby))

'''
四、Python运算符：
1.算术运算符：+ - * / % **
'''
print(10+20) #两个数字相加
print("love"+"Tricy") #两个字符串的拼接
print(str(123)+"abc")
# int - -》str ： str() - --强制字符串的转化, int() - --整型，float(), bool()
print(30 - 10) #两个数字的相减
print(2 * 3) #两个数字的相乘
print("I love you" * 3000) #字符串的重复输出 *次数
print(10 / 2) #结果是浮点数
'''
2.赋值运算符：= += -=  : 方向性--- 右边赋值左边
'''
a = 10
a += 10  # 等同于 a = a + 10
a -= 5   # 等同于 a = a - 5
print(a)
'''
3.比较运算符：< <= > >= == !=  ---运算结果是布尔值
'''
print(2 > 3)
print("登录成功" == "登录成功")  #判断字符串是否相同 === 执行结果  vs  预期结果
'''
4.逻辑运算符：与--and==真真为真   或--or==假假为假    非--not 
'''
print(2 > 3 and 3 < 4)
'''
5.成员运算符：in , not in  -----运算结果都是布尔值True  False
'''
str2="python"
print("Y" in str2)
'''
6.input() ----内置函数：在控制台输入数据--赋值给num变量
'''
# num = input("请输入你的数字：")
# print(num)


'''
作业：
（1）在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台：
'''
# in_name=input("请输入姓名：")
# in_age=input("请输入年龄：")
# in_sex=input("请输入性别：")
# print('''*******************
# 姓名：{0}
# 性别：{1}
# 年龄：{2}
# *******************
# '''.format(in_name,in_sex,in_age))

'''
（2）现在有字符串：str12 = 'python hello aaa 123123aabb'
    1）请取出并打印字符串中的'python'。
    2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
    3）替换python为 “lemon”.
    4) 找到aaa的起始位置
'''
str12 = 'python hello aaa 123123aabb'
print(str12[:6:])
print('o a' not in str12)
print('he' not in str12)
print('ab' not in str12)
print(str12.replace("python","lemon"))
print(str12.find('aaa'))











