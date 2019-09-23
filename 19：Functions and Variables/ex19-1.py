def classroom(student, teacher, desk, chair):
    print(f"In the classroom, we have {student} students and {teacher} teachers.\nHowever, we just have {desk} desks and {chair} chair.\nWhat should we do ? \nI hope that you can help me, Thank you.\n")

print("one")
numstu = int(input())
numteacher = int(input())
numdesk = int(input())
numchair = int(input())
classroom(numstu, numteacher, numdesk, numchair)


print("two")
classroom(10, 20, 5, 5)

print("three")
classroom(numstu + 20, 20, 20, 20)

print("four")
# 输入四个以空格分割的整数，分别赋值给变量numstu1, numtea, numd, numc
numstu1, numtea, numd, numc = map(int,input().split())
classroom(numstu1, numtea, numd, numc)
# print(type(numstu1))

print("five")
# 输入以空格分割的整数（4个），赋值给num1
num1 = map(int,input().split())
classroom(*num1)

print("six")
# 把输入以逗号分隔并转换为int，返回一个元组，每个变量对应一个值
a, b, c, d = (int(x) for x in input().split(','))
classroom(a, b, c, d)

print("seven")
# 把输入以逗号分隔并转换为int，返回生成器
num2 = (int(x) for x in input().split(','))
classroom(*num2)

print("eight")
# 把输入以逗号分隔并转换为int，返回一个列表
num3 = [int(x) for x in input().split(',')]
classroom(*num3)

print("nine")
num4 = input().split(';')
conv = []
for i in num4:
    # print("i: ",i,">>>写入列表前:",conv)
    conv.append(int(i))
    # print("i: ",i,"<<<写入列表后:",conv)
classroom(conv[0],conv[1],conv[2],conv[3])
# num：以；区分的数值输入，conv是一个空列表, for i in num 遍历num，用append()输入conv

print("ten")
stu, t, de, ch = 10, 20, 30, 10
classroom(stu, t, de, ch)
# print(type(stu))