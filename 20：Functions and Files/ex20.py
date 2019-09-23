from sys import argv

script, input_file = argv                                       # 将变量参数argv解包，并依次赋值给script和input_file变量，此时input_file的name属性是文档名

def print_all(f):
    # print(">>>> f:",f)
    print(f.read())                                             # 创建名称为print_all，内含参数f的函数，执行命令：打印f的内容
    # print("<<<<< f:",f)

def rewind(f):
    f.seek(0)                                                   # 创建rewind函数（倒带），将f的指针放回位置0，也就是最开始的位置

def print_a_line(line_count, f):
    # print(">>> line_count:", line_count)
    print(line_count, f.readline())                             # 创建print_a_line函数，有两个参数，执行命令：打印f的一行内容
    # print("<<< exit function print_a_line")

# # 去掉输出空行
# def print_a_line(line_count, f):
#     print(line_count, f.readline(), end='')

# def print_a_line(line_count, f):
#     print(line_count, f.readline().strip())

# def print_a_line(line_count, f):
#     print(line_count, f.readline().split('\n')[0])

# def print_a_line(line_count, f):
#     print(line_count, f.readline().replace('\n', ''))

current_file = open(input_file)                                 # 打开文件并返回文件对象，文件对象可以阅读文件，但是不是文件本身

print("First let's print the whole file:\n")

print_all(current_file)                                         # 调用print_all函数，读文档内容

print("Now let's rewind, kind of like a tape.")
# print(">>> 执行rewind之前指针位置：",current_file.tell())
rewind(current_file)                                            # 将指针归零，如不进行此操作，read()执行后，指针在最后，再执行readline()返回空
# print("<<< 执行rewind之后指针位置:",current_file.tell())

print("Let's print three lines:")

current_line = 1                                                # 1 赋值给current_line，此时参数line_count值为1
print_a_line(current_line, current_file)                        # 调用print_a_line，读第一行
# print(">>> 读完第一行当前指针位置：",current_file.tell())

current_line = current_line + 1                                 # 1 + 1 赋值给current_line，此时参数line_count值为2
print_a_line(current_line, current_file)                        # 再次调用，读下一行
# current_line += 1
# print(">>> 读完第二行当前指针位置：",current_file.tell())

current_line = current_line + 1                                 # 2 + 1 赋值给current_line，此时参数line_count值为3
print_a_line(current_line, current_file)                        # 再次调用，读下一行
# print(">>> 读完第三行当前指针位置：",current_file.tell())

# # 代替Let's print three lines:后面的内容
# num = len(current_file.readlines())
# rewind(current_file)

# print("Let's print three lines:")
# for i in range(1, num+1):
#     print_a_line(i, current_file)
