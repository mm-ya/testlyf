"""
print("呜呜呜呜",end="嘤嘤嘤")
print (2333)
print(2.333)
name="王五"
r=2+3-2*3

# print (name,r)
#a=input("请输入值")

# print("这是我输入的值",a)
a=int(input("第一个数"))
b=int(input("第二个数"))

print("两数之和",float(a)+float(b))


a=input("hhhhhhh")
b=len(a)
if b%2==0:
   print ("偶数")
else:
 print ("奇数")

b=(1,3,5,"嘤嘤嘤")#必须顶格写
a=(1,2,3,4,5,6,True,b)# 元组
print(a[3])
# 下标从左到右 0........
# 下标从右到左 -1 ......
print(a.index(2))
# index() 获取下标
print(a.count(1))
# count（） 获取出现的个数

print(a[-1][-1])#二维元组
print(a[0:3])   #切片 左闭右开
# 元组与数组的操作一模一样，区别是元组不可以修改，数组可以修改

b=(1,3,5,"嘤嘤嘤")
a=[1,2,3,4,5,6,b]
name=input("输入")
a.append(name)#增加列表（在末尾）
a.insert(3,name)#插入到列表指定位置
print(a)
ss=a.pop(6)#提取数据
print(ss)
c=["m","y"]
a.extend(c)#列表整合
print (a)
 """
d=[1,2,3,4,5,6]
#d.sort(reverse==true)
print(d)
d.reverse

print(d)
d.clear(2)
print(d)
