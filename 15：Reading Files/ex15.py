from sys import argv

# 命令行输入
script, filename = argv

# 打开文件，并且返回文件操作对象
txt = open(filename) # 有的时候open需要添加参数：encoding = "utf-8"
# print(">>>txt:",repr(txt)) 
# txt.close()

# 使用 f-string 调用 filename
print(f"Here's your file {filename}:")
# 读取整个文件，将文件内容放到一个字符串变量中。
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)
# print(txt.read() == txt_again.read()) # false

print(txt_again.read())
txt_again.close()