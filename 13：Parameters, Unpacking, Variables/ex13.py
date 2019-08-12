# argv:argument vector/variable(参数向量、参数变量) 
# 告诉 python 从 sys（系统） module 取出 argv 功能，这样就可以获取命令行参数
from sys import argv
# 在运行命令时，需要加入参数，输入三个参数，script旨在ex3.py,
# 若没有输入参数，运行会出错，参数不足，若输入超过所需参数，报错说参数过多
script, first, second, third = argv
first = int(first)

# # 可以通过print了解argv是什么
# print(">>>>argv:", repr(argv))

# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# print(">>>argv:", int(argv)) 

a = input("How do you feel about this exercise?")
print("A different way to say so:", end=' ')
b = input() # 如果需要int()，在这里转换，在f中转换，如果出错难以寻找
print(f"one way: {a} and another way: {b}")


print("The script is called:", script)
print(f"The script is called: {script}")

print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



print(f"{script} {first}")
print(f"{first + second}") # 字符串相连

# 20行数值只能是整数，21行可以是浮点数
print(f"{first+int(second)}") # 可以将这里的转化放到输入时进行
print(f"{eval(first)+eval(third)}")

print("{}+{}".format(int(first),int(second)))
print("{}".format(int(first)+int(second)))