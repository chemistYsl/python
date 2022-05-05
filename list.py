# []表示列表，用逗号隔开
fruits = ['banana', 'apple', 'pear']
print(fruits)
# 将整个等号后面的都输出

# 访问列表中元素
print(fruits[0])
# 只输出元素

# 修改元素
fruits[0] = 'watermelon'
print(fruits)

# 添加元素
# 末尾
fruits.append('banana')
print(fruits)
# 插入
fruits = ['banana', 'apple', 'pear']
fruits.insert(0, 'watermelon')
print(fruits)

# 删除
# del语句
fruits = ['banana', 'apple', 'pear']
del fruits[0]
print(fruits)
# pop语句删除末尾元素，可使用删除元素
fruits = ['banana', 'apple', 'pear']
last_fruit = fruits.pop()
print(fruits)
print('my fruit is ' + last_fruit + '.')
# pop也可以删除任意元素，用法于del一样
# 根据值删除元素remove,若值多次出现，需循环语句删除
fruits = ['banana', 'apple', 'pear']
fruits.remove('pear')
print(fruits)
fruits = ['banana', 'apple', 'pear']
delt = 'banana'
fruits.remove(delt)
print(delt)

# 列表永久排序sort
fruits = ['banana', 'apple', 'pear']
fruits.sort()
print(fruits)
# 相反排序fruits.sort(reverse = true)
# 临时排序sorted
fruits = ['banana', 'apple', 'pear']
print(fruits)
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))

# 倒着打印 reverse()
fruits = ['banana', 'apple', 'pear']
fruits.reverse()
print(fruits)

# 长度 len（）
fruits = ['banana', 'apple', 'pear']
a = len(fruits)
print(a)

# 访问最后一个元素 fruits[-1]
