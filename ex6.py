# 给 types_of_people 赋值：10
types_of_people = 10
# 将字符串赋值给 x ，使用 f-string 将 type_of_people 嵌入 x 中
x = f"There are {types_of_people} types of people."

# 赋值
binary = "binary"
do_not = "don't"
# 赋值并嵌入
y1 = f"Those who know {binary} and those who {do_not}."
y2 = "Those who know " + binary + " and those who " + do_not + '.'

# 打印输出
print(x)
print(y1)
print(y2)

# 插入变量值打印输出
print(f"I said: {x}")
print(f"I also said: '{y1}'")

# 赋值
hilarious = False
# 1赋值，format 使用{}转义
# 2为正常赋值
joke_evaluation1 = "Isn't that joke so funny?! {}"
joke_evaluation2 = "Isn't that joke so funny?! "


print(joke_evaluation1.format(hilarious))
print(joke_evaluation2 + f"{hilarious}")
# print(f"{joke_evaluation2 + hilarious}") 不可以，因为hilarious是Boolean类型，joke_evaluation是string类型 
print(f"{joke_evaluation2}" + f"{hilarious}")

w = "This is the left side of..."
e = "a string with a right side."

# 连接两个字符串组成更长的字符串
print(w + e)