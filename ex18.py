def print_two(*args):
    arg1, arg2 = args                                         # 1-line1
    print(f"args1: {arg1}, args2: {arg2}")                    # 1-line2
    # print("arg1: {}, arg2: {}".format(*args)) # 可以运行     # 2
    
    # j = 1                                                   # 3-line1
    # for i in args:                                          # 3-line2
    #     print(f"agr{j}:",i,end = " ")                       # 3-line3
    #     j = j+1                                             # 3-line4
    # # ?使用\n会有很大行距，但是使用\t就没有行距，并且可以换行
    # print('\t')                                             # 3-line5
    
    # print(f"args1: {*args}, args2: {*args}") # 报错

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

# a, b, c, d = input().split() # 对于for循环，*，输入多少参数都可以
# print_two(a, b, c, d)

a, b= input().split()   
print_two(a, b)

print_two("Zed","Shaw") # 如何更改为输入显示input()?
print_two_again("Zed","Shaw")
print_one("First!")
print_none()