# 输出列表所有元素
fruits = ['banana', 'apple', 'pear']
for fruit in fruits:
    print(fruit)

# 创建数值列表
# range 函数
for i in range(1, 5):
    print(i)

# 列表list（）将range（）转化
numbers = list(range(1, 5))
print(numbers)
# 指定步长
numbers = list(range(1, 21, 3))
print(numbers)
# 平方加入空列表
squares = []
for i in range(1, 11):
    square = i**2
    squares.append(square)
    # squares.append(i**2)
print(squares)
# 列表解析，简洁代码生成列表
squares = [i**2 for i in range(1, 11)]
# i**2为表达式，for语句给表达式赋值
print(squares)

# 使用列表一部分 切片






