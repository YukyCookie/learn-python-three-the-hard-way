def add(x1, y1):
    x1 + y1

def add2(x2, y2):
    return x2 + y2

def add3(x3, y3):
    print(x3 + y3)

def add4(x4, y4):
    return print(x4 + y4)

def add5(x5, y5):
    print(x5 + y5)
    return x5 + y5

print(add(1, 2)) # 输出none，因为没有返回值，所以print输出默认none
print(add2(1, 2)) # 输出3，有返回值能输出
print(add3('a', 'b')) # 输出ab和none，输出ab是因为函数执行就会有输出，输出none是打印add3(x3, y3)这个函数，没有返回值
print(add4('c', 'd')) # 与add3函数等价，所以结果意义一致，猜测：虽然有返回值，但是返回值是打印输出，所以返回none
print(add5(2, 4)) # 输出6和6，第一个6是执行add5函数，第二个6是打印add5函数，该函数有返回值，则打印出来


