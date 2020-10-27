'''
常用数据类型续 ： 列表（list）   元组   字典   集合
列表（list）： []，元素和元素之间用英文的逗号隔开
(1)列表元素可以是任意的数据类型：int  flost  bool  str  list ......
(2)取值：索引取值---类比字符串
取多个值：切片---类比字符串
扩展：列表的嵌套取值
(3)列表的元素是可以被改变的！----增加，修改，删除   --重点
(4)列表元素是可以重复的  -----统计个数count()
(5)len()   ---- 统计元素个数
'''
# list1 = [] #可以为空列表
# list1 = [20,3.14,True,"七木","荷花鱼",[1,2,3,4]]
# print(list1)
# print(list1[3])  #索引取值，结果：七木
# print(list1[3:5:1])  #切片，结果：['七木', '荷花鱼']---还是一个list
# print(list1[5][1])  #列表的嵌套取值,结果：2
#
# #列表的增加
# list1.append("焕蓝")   #默认追加元素到列表的末尾  ---p1
# list1.insert(5,"kingo")  #指定位置进行元素插入  ---p2
# list1.extend(["十又","bingo","陌上寸草","大丑"])  #两个列表合并  ---p3
# print(list1)
#
# #删除
# list1.pop(0)   #默认删除最后一个元素，也可以指定位置（索引）进行删除
# list1.remove(3.14) #指定一个元素本身进行删除
# # list1.clear()  #清楚所有元素，就会变成一个空列表
# print(list1)
#
# #修改
# list1[4] = "Amiee"
# list1[0] = "方方土"
# print(list1)
# #列表元素是可以重复的
# list1.append("方方土")
# print(list1)
# print(list1.count("方方土"))  #统计个数count()
# print(len(list1))  #统计元素个数

'''
元组：tuple，()
(1)元组元素可以是任意的数据类型：int  flost  bool  str  list tuple......
(2)取值：索引取值---类比字符串
取多个值：切片---类比字符串
扩展：列表的嵌套取值
(3)元组的元素是不可以被改变的！
(4)元组元素是可以重复的  -----统计个数count()
(5)len()   ---- 统计元素个数
(6)list   tuple  互换  ----扩展
'''
# tuple1 = ('方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝', '十又', 'bingo', '陌上寸草', '大丑')
# # tuple1[-1] = '小丑'   #  ---不可以，会报错，元组元素不可以改变
# print(tuple1.count("大丑"))
# #如果要改变元组的元素，可以先将元组转换成列表，修改元素之后，再转成元组
# list2 = list(tuple1)  #把元组转换成列表
# list2[-1]="小丑"
# print(list2)
# tuple2 = tuple(list1)
# print(tuple2)

'''
字典：dict   {}
(1)元素：key:value  (键值对)
(2)场景：存储数据属性：人---名字  身高  体重
    key：1)不能是可以改变的数据类型(list、dict) ----字符串；
         2)不能重复的，是唯一的
    value：可以是任意数据类型---可以被改变 === 增删改
(3)字典是没有顺序的！！！ ---不能用索引取值
    ----取值：通过key  取value
(4)len()-----长度
'''
# dict1 = {"name":"tan","height":"173","weight":"160"}   #可以为空字典
# #字典取值
# print(dict1["height"])     #方法一,key——value
# print(dict1.get("weight"))  #方法二,key——value
# #修改对应key的value值
# dict1["weight"]=150
# print(dict1["weight"])
# #增加
# dict1["age"]=18  #如果key不存在，新增加键值对；如果key存在，则修改对应key的value值
# print(dict1)
# dict1.update({"city":"北京","hobby":"学习Python","gender":"male"})  #增加多个键值对
# print(dict1)
# #删除
# dict1.pop("weight") #字典没有顺序，所以不存在最后的元素，必须指定key删除对应的键值对
# print(dict1)
# del dict1  # 变量存储   删除---对象不存在了

'''
集合：set  {}，元素是单个的   -----了解
(1)无序的
(2)元素不可以重复 ————使用场景：去重
'''
# list3={11,22,11,33,11,11}
# #去重
# set1 = set(list3)  # set() ---  list3转为集合
# print(set1)
# list4 = list(set1)
# print(list4)

'''
控制流：代码的执行顺序 -----从上至下，依次执行：判断   循环
判断： if  语法
if 条件:   -----成立-----冒号:缩进（4个空格=tab键）
    子代码（执行语句）
elif 条件:   -----成立 
    子代码（执行语句）
...（elif可以没有，可以有多个）
else: (后面没有条件--兜底)   ----以上都不符合，执行，可以没有else
    子代码（执行语句）
'''
# money = int(input("请输入你的余额："))  #input()控制台输入----数据类型---字符串
# if money >= 500:
#     print("买别墅")
# elif money >=200:
#     print("买一栋楼")
# elif money >=50:
#     print("买车！")
# else:
#     print("滚去工作赚钱")
#
# # dict()  --内置函数，生成字典
# dict1 = {"name":"Tricy","age":"18"}
# dict2 = dict(name="Tricy",age="18")
# print(dict1)
# print(dict2)

'''
作业：
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面
'''
a=[1,2,'6','summer']
if "i" in a:
    print("i是成员")
else:
    print("i不是成员")

'''
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
'''
dict_1={"class_id":45,'num':20}
num = dict_1['num']
if num>5:
    print("班级上课人数为：{}".format(num))
else:
    print("班级上课人数小于等于5")
'''
3、list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。
并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；
方法2： 自动--dict（）
'''
#方法1：
list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
list2 = [{"name":"方方土","sex":"男","age":"18","city":"上海"},
         {"name":"七木","sex":"男","age":"18","city":"上海"},
         {"name":"荷花鱼","sex":"男","age":"18","city":"上海"},
         {"name":"kingo","sex":"男","age":"18","city":"上海"},
         {"name":"Amiee","sex":"男","age":"18","city":"上海"},
         {"name":"焕蓝","sex":"男","age":"18","city":"上海"}]
print(list2)
#方法2：
list2 = ["男","男","女","女","男","男"]
list3 = [18,19,20,21,22,23]
list4 = ["上海","北京","成都","重庆","江苏","上海"]
list5 = []
for i in range(0,6,1):
    dict1=dict(name=list1[i],sex=list2[i],age=list3[i],city=list4[i])
    list5.append(dict1)
print(list5)






