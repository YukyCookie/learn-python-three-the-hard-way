# 将一个文档的内容复制到另一个文档
from sys import argv
from os.path import exists
# 在运行程序之前需要具体填入文件名，如果文件名不存在，则会新建一个文件
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# open(to_file,'w').write(open(from_file).read())
# ,encoding="utf-16" 不可以为encoding = "unicode"
in_file = open(from_file,encoding="utf-16")
print(repr(in_file))

indata = in_file.read()
# print(type(indata))
# print(">>>>>indata:",repr(indata))

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL_C to abort.")
input()

# 如果文件不存在，到这一步to_file代表的文件才正式建立。
out_file = open(to_file, 'w')
print(">>>>>to_file", repr(to_file))

# print(f"{exists(to_file)}")
# print(">>>out_file:",repr(out_file))
out_file.write(indata)
# print(f"{exists(to_file)}")

# out_file = open(to_file, 'wb')
# out_file.write(indata)

print("Alright, all done.")

# out_file.close()
# in_file.close()