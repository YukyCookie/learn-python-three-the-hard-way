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
  
* ### 学习内容：`.format()`；`repr()`

  * #### `.format()`

    * 可以接受不限个参数，位置可以不按顺序。
    
    * 不指定位置
    
      输入：
    
      ```python
      print("{} {}".format('a', 'b'))
      
      c = "{} {}"
      print(c.format('a', 'b'))
      ```
    
      结果：
    
      ```powershell
      a b
      a b
      ```
    
      第一段和第二段等同，没有指定位置，所以按照默认顺序输出
    
    * 指定位置
    
      输入：
    
      ```python
      print("{1} {0}".format('a', 'b'))
      
      c = "{1} {0}"
      print(c.format('a', 'b'))
      
      print("{b} {a}".format(a=1, b=2))
      
      site = {"a": 1, "b": 2}
      print("{a} {b}".format(**site))
      
      my_list = ["num1", "num2"]
      print("{0[1]} {0[0]}".format(my_list))
      ```
    
      结果：
    
      ```powershell
      b a
      b a
      2 1
      1 2
      num2 num1
      ```
    
      第一段，0位置存储的是`a`，1位置存储的是`b`，大括号中的数字代表读取内容的存储位置。
    
      第二段，与第一段等同。
    
      第三段，在`format()`中设置参数和参数内容，在前面的大括号里面指定要输出的参数值。
    
      第四段，通过字典设置参数。
    
      第五段，通过列表索引设置参数。
    
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

  * #### 参数个数<大括号个数

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
    
  * #### 参数个数>=大括号个数
    
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




