def classroom(student, teacher, desk, chair):
    print(f"In the classroom, we have {student} students and {teacher} teachers.\nHowever, we just have {desk} desks and {chair} chair.\nWhat should we do ? \nI hope that you can help me, Thank you.\n")

print("one")
# 疑问，是否可以a,b,c,d = int(input()) 如何修改
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
numstu1, numtea, numd, numc = map(int,input().split())
classroom(numstu1, numtea, numd, numc)
# print(type(numstu1))

print("five")
# 为什么要加括号
a, b, c, d = (int(x) for x in input().split(','))
classroom(a, b, c, d)

print("six")
num = input().split(';')
conv = []
for i in num:
    print(i)
    conv.append(int(i))
classroom(conv[0],conv[1],conv[2],conv[3])
# num：以；区分的数值输入，conv是一个空数组, for i in num 遍历num，用append()输入conv

print("seven")
stu, t, de, ch = 10, 20, 30, 10
classroom(stu, t, de, ch)
# print(type(stu))

print("eight")

