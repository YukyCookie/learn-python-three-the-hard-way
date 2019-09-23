# def num(a):
#     print(">>>> a:", a)
#     return 1

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
    # print(f"ADDING {a} + {b}", a + b) 
    # # 只运行此行会在下面报错，unsupported operand type(s) for +: 'NoneType' and 'float'
    # # nonetype类型是指参数为空，之所以为空，是因为age没有返回任何值

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

a, b, c, d, e, f, g, h = map(int, input().split(','))

age = add(a, b)
height = subtract(c, d)
weight = multiply(e, f)
iq = divide(g, h)


# sometry = num(30)
# print(sometry)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle")

# height - iq / 2 * weight + age
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# 24 + 34 / 100 - 1023
test1 = add(24, subtract(divide(34, 100), 1023))
print(test1)

# weight + iq * iq - height / age * iq + age
test2 = add(age, add(weight, subtract(multiply(iq, iq), divide(height, multiply(age, iq)))))
print(test2)