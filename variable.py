# 修改字母大小写
# 首字母大写
name = "ada lovelace"
print(name.title())

# 字母大写
name = "ada lovelace"
print(name.upper())

# 字母全大写
name = "ada lovelace"
print(name.lower())

# 字符串连接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello " + full_name.title() + "!")

# 制表符和换行符
print("\tpython")
print("\npython")

# 删除空白
name1 = 'python '
print(name1)
print(name1.rstrip())
# 删除后面空白
# 去除空白只是暂时的，将变量重新赋值才会永久去掉空白
name1 = name1.rstrip()
print(name1)
# 空白没了
name1 = ' python '
print(name1)
name1 = name1.rstrip()
print(name1)
name1 = name1.lstrip()
print(name1)
name1 = name1.strip()
print(name1)
# str()避免类型错误
