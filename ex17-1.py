from sys import argv 
script, t1_file,t2_file = argv

a = open(t1_file,'r',encoding = "utf-16")
print(a.read())
b = open(t1_file,'rb')
print(repr(b.read()))

c = open(t2_file,'r')
print(c.read())
d = open(t2_file,'rb')
print(d.read())