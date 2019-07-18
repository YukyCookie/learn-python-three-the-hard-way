# a = input("age:") # 数据类型为string
# print(type(a)) # 返回数据类型
# b = int(input("age:")) # 数据类型强制转换为整数型
# print(type(b))


# 有end=' '，问题和输入内容在同一行，否则输入内容会在下一行出现
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# a = input("What's your name?")
# print(
# f"""Hello,{a}!
# {a},Let's add this two number
# """)

# b = input("Get the first number:")
# c = input("Get the second number:")
# d = b + c
# print(d)

# e = int(b) + int(c)
# print(e)

