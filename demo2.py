
a={"name":"张三","sex":"男"} #{key:value}
print(a["sex"])
"""
字典没有下标的概念
说明字典没有顺序的说法
字典取值，输key
"""

# 取值
print(a["sex"])#当key1不存在时，报S错
print(a.get("name1"))# 当key不存在 输出None
# 新增和修改、
a["name"]="李四"# key不存在时，就会新增，当key存在时，就修改
a.update(address="雅安")# update的写法的时候 ，key在这里时一个变量的写法
print(a)
print(list(a.values()))