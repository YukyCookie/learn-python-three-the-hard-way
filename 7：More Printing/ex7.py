print("Mary had a little lamb.")
# 使用format将snow 加入句子中
print("Its fleece was white as {}.".format('snow'))
# 转化为f-string：print (f"Its fleece was white as {'snow'}.")
print("And everywhere that Mary went." )
# 打印 . 十次
print("." * 10)


end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# print默认是打印一行，结尾加换行。
#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)