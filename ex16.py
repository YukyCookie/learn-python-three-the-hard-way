from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
# line 7,8 有什么意义？
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.") 

input("?")

print("Opening the file...")
# w 新建只写，w+ 新建读写，二者都会将文件内容清零（以 w 方式打开，不能读出。w+ 可读写）
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()
# print(repr(target.truncate()))

print("Now I'm going to ask you for three lines>")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 改写成一条命令
# target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write("{}\n{}\n{}\n".format(line1,line2,line3))

# # 要在open参数为'w+'才能运行，否则会报错，因为在这个时候文档还是空，内容还在内存中，要关闭后才能将内容写入文档
# print(target.read()) 

# 此时内容才写入文件
print("And finally, we close it.")
target.close()

target = open(filename)
print(target.read())
target.close()