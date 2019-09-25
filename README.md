# 目录

每个练习涉及的知识点列表如下：

| 题号 | 学习内容                                                     | 改变代码                                                     |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | `print()`；`#`；                                             | `print`<br/>`print(`<br/>`print("`<br/>在代码开始输入空格    |
| 2    | `print()`；`#`；                                             | `#`放入字符串中                                              |
| 3    | `+`、`-`、`/`、`*`、`%`、`<`、`>`、`<=`、`>=`、              | `++i/--i`<br/>python没有自增自减符号(`++`/`--`)              |
| 4    | 变量；`=`；`_`                                               | 变量名不一致<br/>同一变量名赋值两次<br/>`print()`中缺了逗号<br/>运算式可以在`print()`中执行 |
| 5    | `f`基本概念；`+`<br/>`round()`                               | `f`嵌套；`+`连接                                             |
| 6    | `f`基本概念；`,format()`与`f`互换<br/>用`print`进行debug     | 不同类型的数据不能用`+`连接<br/>单引号和双引号的混合使用；   |
| 7    | `print(变量名或"字符串", end='')`<br/>`print("." * 10)`      | `format`和`f-string`相互转换                                 |
| 8    | `.format()`参数位置和个数<br/>`repr()`                       | `.format()`参数个数<大括号个数<br/>`.format()`参数个数>=大括号个数<br/>`python3`字典<br/>`python3` 列表 |
| 9    | `\n`；`"""`(三引号)                                          | 在双引号或者单引号中使用回车换行，会报错；                   |
| 10   | 转义字符（含义及例子）                                       |                                                              |
| 11   | `input()`；`eval()`                                          | `int(input())`和`eval(input())`<br/>`eval()`（输出数字，字符串，和引号的关系） |
| 12   | `pydoc`                                                      | `input()`和`f-string`或`.format()`结合                       |
| 13   | `argv`                                                       | `argv`脚本输入参数与要求输入个数不符<br/>用`f-string`改写ex13.py代码<br/>强制转换数据类型用在变量赋值时更好 |
| 14   | `argv`和`input`结合运用                                      |                                                              |
| 15   | `open()`；`close()`；`read()`；                              | 关闭文档后再读取文档（执行`close()`后再执行`read()`)<br/>保存txt文档不是`utf-8`编码会导致无法读取<br/>用`repr()`来查看不懂的地方 |
| 16   | `readline()`；`write()`；`seek()`；`truncate()`<br/>`open()`中的`w`、`wb`、`w+`、`r`、`rb`、`r+`、`a`、`a+`； | 在`r`的情况下尝试执行写入命令（执行`.write()`<br/>执行`.truncate()`）<br/>在`w`的情况下尝试执行读取命令<br/>执行`close()`后再对文档进行读写操作 |
| 17   | `len()`；`exists()`；                                        | 直接用`echo`创建文档，读写时的问题（ex15有稍微提到）<br/>`import`机制<br/>`Unicode(UTF-8,UTF-16)` |
| 18   | 函数(`def`)                                                  | 用`from sys import argv`改写可以任意输出参数<br/>用`input()`改写<br/>用`.format()`代替`f-String`<br/>用`for`循环扩充输入的参数数量 |
| 19   | `map()`（`sorted()`返回列表）；`split()`<br/>元组`tuple`；列表`list`；生成器；`list.append()` | 运行函数的方法（10种）                                       |
| 20   | `range()`；`strip()`；`replace()`；                          | 缩减`print("Let's print three lines:")`后面的代码<br/>修改函数`print_a_line()`去掉上述输出结果中的空行（4种方法）<br/>`.split()[0]`； |
| 21   | `return`                                                     | 函数中有无`return `的差别<br/>复杂运算表达式；               |
| 23   | `.encode()`；`.decode()`                                     | 用不同编码解读文档（选取部分文本）（`utf-8`，`utf-16`，`utf-32`）<br/>以其他形式编码的文本运行此代码<br/>给一个不存在的编码标准<br/>重写代码(`b''`bytes)<br/>在重写基础上删减字节（以utf-8编码的为例）<br/>Unicode编码（utf-8,utf-16,utf-32）使用字节数 |
| 24   | 复习转义字符；三引号；运算表达<br/>`f-string`；`.format()`   |                                                              |
| 25   | 复习函数；`sorted()`；`list.pop()`<br/>字典`pop()`（注意`default`的使用） | 尝试`help(ex25)`和`help(ex25.break_words)`<br/>尝试调用`ex25.py`中的某一函数（`from ex25 import break_words`）<br/>`import`，`from···import *`，`from···import··· `的区别 |
| 26   | 测试：修改错误                                               |                                                              |
| 27   | `not`；`or`；`and`；`not or`；`not and`；`!=`；`==`          |                                                              |
| 28   | 比较运算符；运算符优先级；                                   | 无法识别`true`、`false`<br/>`1 and 1`返回`1`，`False and 1`返回`False`<br/>按位取反（未补充完全） |
| 29   | `if`基本概念                                                 | 为什么if下面的代码需要缩进四个格？<br/>如果if下面的第一行代码不缩进，会报错。<br/>如果if下面的多行代码缩进不对齐，会报错。<br/>如果if下面的第二行及往后的代码不缩进，不会报错。<br/>将其他的Boolean表达运用到`if`语句中<br/>如果改变练习中的变量值 |
| 30   | `if-elif-else`                                               | 尝试使用更复杂的Boolean 表达<br/>如果有多个`elif`都为`True`  |
| 31   | `if`嵌套                                                     | 写入模仿的游戏（`eval()`；`range()`和用比较运算符划定数字范围的区别） |
| 32   | `for`循环（else，循环变量作用域）；`list`<br/>`list.append(obj)`<br/>`list.count(obj)`<br/>`list.extend(seq)`<br/>`list.index(obj)`<br/>`list.insert(index, obj)`<br/>`list.pop([index=-1])`<br/>`list.remove(obj)`<br/>`list.reverse()`<br/>`list.sort(key='', reverse=False)`<br/>`list.clear()`<br/>`list.copy()` | 练习中第22行代码直接用`range(0, 6)`创建列表<br/>`range()`在ex20：Functions and Files中有详细说明 |