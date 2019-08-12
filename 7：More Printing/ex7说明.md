# EX7: More Printing

* ### 例子：

  ```python
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
  ```

* ### 学习内容：`print(变量名或"字符串", end='')`；`print("." * 10)`

  * #### `print(变量名或"字符串", end='\n')`

    * `end`为用来设定以什么结尾。当`print`不设定`end`的属性值时，默认值是换行符 \n。所以`print()`输出默认换行。引号中可以换成其他字符串。

    * 设置不同的属性值：

      1. 设置`end=' '`时，`print()`输出不换行，以空格结尾。
      2. 设置`end=''`时，`print()`输出不换行，以无字符结尾。
      3. 设置`end='*'`时，`print()`输出不换行，以`*`结尾。
  
      输入：
      
      ```python
      print("Cheese", end=' ')
      print("Burger", end='<<<end')
      ```
      
      结果：
      
      ```powershell
      Cheese Burger<<<end
      ```
      
      输出Cheese，以空格结尾不换行。接着空格后面输出Burger，以设置的字符串`<<<end`结尾，也是不换行的。
      
      若想以字符串结尾同时换行，可以设置为`print("你想要输出的东西", end='你想用来结尾的字符串\n')`这样就可以做到换行。

  * #### `print("." * 10)`

    * 打印输出10个`.`
    
    * 引号中的是要重复的字符串，数字代表需要重复的次数
    
      输入：
    
      ```python
      print("+" * 10)
      print("a" * 5)
      print("a " * 5)
      print("b\n" * 3)
      ```
    
      结果：
    
      ```powershell
      ++++++++++
      aaaaa
      a a a a a
      b
      b
      b
      ```
    
      第一行，输出10个`+`
    
      第二行，输出10个`a`
    
      第三行，引号中`a`后面有空格，所以输出结果有间隔
    
      第四行，引号中包含了换行符，所以结果换行输出
    

* ### 改变代码（寻找可能情况及错误）

  * #### `format`和`f-string`相互转换

    输入：

    ```python
    print("Its fleece was white as {}.".format('snow'))
    print(f"Its fleece was white as {'snow'}.")
    ```

    结果：

    ```powershell
    Its fleece was white as snow.
    Its fleece was white as snow.
    ```

    大部分情况都可以相互转换。




