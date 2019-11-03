# EX8: Printing，Printing 

* ### 例子：

  ```python
  formatter = "{} {} {} {}"
  
  print(formatter.format(1, 2, 3, 4))
  print(formatter.format("one", "two", "three", "four"))
  print(formatter.format(formatter, formatter, formatter, formatter))
  print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
  ))
  ```
  
* ### 学习内容：`.format()`参数位置和个数；`repr()`

  * #### `.format()`

    * 可以接受不限个参数，位置可以不按顺序。
    
    * 不指定位置
    
      输入：
    
      ```python
      print("{} {}".format('a', 'b'))
      
      c = "{} {}"
      print(c.format('a', 'b'))
      
      my_list = ["num1", "num2"]
      print("{} {}".format(*my_list))
      
      my_list = ("num1", "num2")
      print("{} {}".format(*my_list))
      ```
    
      结果：
    
      ```powershell
      a b
      a b
      num1 num2
      num1 num2
      ```
    
      第一段和第二段等同，没有指定位置，所以按照默认顺序输出。
    
      第三段是列表，可以用`*`批量传参。
    
      第四段是使用`*`元组传参。
    
    * 指定位置
    
      1. `format`参数情况是以下其中一种：
    
         * 只有不可变数据类型变量（一个，多个都可以）`format('a','b')`
      
         * 只有可变数据类型变量（列表，元组，字典）（一个）`format(*list)`
      
         那么，形式为：**`{}`中写入索引值指代位置，若是字典，写入key，输出key对应的值**。
      
      输入：
      
      ```python
      # 0位置存储的是`a`，1位置存储的是`b`，大括号中的数字代表读取内容的存储位置。
      print("{1} {0}".format('a', 'b'))
      
      # 与第一段等同。
      c = "{1} {0}"
      print(c.format('a', 'b'))
      
      # 在format()中设置参数和参数内容，在前面的大括号里面指定要输出的参数值。这里大括号中不能写0，1，会报错。
      print("{b} {a}".format(a=1, b=2))
      
      # 给两个变量赋值，然后作为参数写在format里，用0，1表明输出位置。
      a = 1
      b = 2
      print("{1}, {0}".format(a, b))
      
      # 通过字典设置参数，直接在{}中输入key名称，会输出key对应的值。
      dict1 = {"a": "字典1", "b": "字典2"}
      print("字典：{a} {b}".format(**dict1))
      
      # 通过列表索引设置参数，直接在`{}`中表明参数位置，位置从0开始。
      list1 = ["列表1", "列表2"]
      print("列表：{1} {0}".format(*list1))
    
      # 通过元组设置参数，直接在`{}`中表明参数位置，位置从0开始。
      tuple1 = ("元组1", "元组2")
      print("元组：{1} {0}".format(*tuple1))
    
      var = "你好"
      print("dict1的字典2：{0[b]} , list1的列表1：{1[0]} , tuple1的元组2：{2[1]} , var常量：{3}".format(dict1, list1, tuple1, var))
      ```
      
      结果：
      
      ```powershell
      b a
      b a
      2 1
      2, 1
      字典：字典1 字典2
      列表：列表2 列表1
      元组：元组2 元组1
      ```
    
      2. `format`参数中是多种类型的组合：
      
         * 列表+字典
         * 列表+不可变数据类型变量
         * 元组+字典，等等`format(list, a, tuple)`
          
         
         则指定位置形式为：**`{参数位置[序列中的元素位置]}`**，参数位置指的是在`format`中是第几个参数，位置从0开始，序列中的元素位置指的是在序列中这个元素的索引值是多少，如果是字典，就是key是哪个。
    
      输入：
    
      ```python
      dict1 = {"a": "字典1", "b": "字典2"}
      list1 = ["列表1", "列表2"]
      tuple1 = ("元组1", "元组2")
      var = "你好"
      
      print("dict1的字典2：{0[b]} , list1的列表1：{1[0]} , tuple1的元组2：{2[1]} , var常量：{3}".format(dict1, list1, tuple1, var))
      ```
    
      `{0[b]}`：选择第一个参数`dict1`，是字典类型，选择`dict1`里面`key`为`b`的值
    
      `{1[0]}`：选择第二个参数`list1`，是列表类型，选择`list1`里面的第一个元素值
    
      `{3}`：选择第三个参数`var`
    
      （菜鸟教程中说`{0[1]}`的0是必须的，是错误的，因为不一定是0）
    
      结果：
    
      ```powershell
      dict1的字典2：字典2 , list1的列表1：列表1 , tuple1的元组2：元组2 , var常量：你好
      ```
    
      详细可以参考：<https://blog.csdn.net/jpch89/article/details/84099277>
    
  * #### `repr()`函数
  
    * `repr()`的意思representation。
  
    * 将对象转化为供解释器读取的形式。也就是会把变量的内容原原本本的输出。
  
      输入：
  
      ```python
      s = '2222'
      
      print(s)
      print(repr(s)) 
      ```
  
      结果：
  
      ```powershell
      2222
      '2222'
      ```
  
* ### 改变代码（寻找可能情况及错误）

  * #### `.format()`参数个数<大括号个数

    输入：

    ```python
    formatter = "{} {} {} {}"
    
    print(formatter.format(1, 2, 3))
    ```
  
    结果：
    
    ```powershell
    Traceback (most recent call last):
        File "TEST.py", line 3, in <module>
          print(formatter.format(1, 2, 3))
      IndexError: tuple index out of range
    ```
    
    索引错误：超出了数组的范围。
    
  * #### `.format()`参数个数>=大括号个数
    
    输入：
    
    ```python
    formatter = "{} {} {}"
    
    print(formatter.format(1, 2, 3, 4))
    ```
    
    结果：
    
    ```powershell
    1 2 3
    ```
    
    不会报错，在参数个数<大括号个数时，有多少大括号，就会输出多少参数。
  
* ### 补充知识

    * #### [`python3`字典](https://www.runoob.com/python3/python3-dictionary.html)

        * 字典是一种可变容器模型，且可存储任意类型对象。

        * 格式如下所示：

            `d = {key1 : value1, key2 : value2 }`

            访问时：

            `print(d[key1])`

            如果key1为字符串，需要加引号，如果是数字，则不需要加引号  

            1. 键：key1，key2……    值：value1，value2……

            2. 键是唯一的，键必须是不可变的，如字符串，数字或元组，但是不可以用列表。

            3. 值不需要唯一，可以取任何数据类型

    * #### [python3 列表](https://www.runoob.com/python3/python3-list.html)




