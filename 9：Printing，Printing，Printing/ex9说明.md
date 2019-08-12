# EX9: Printing，Printing，Printing

* ### 例子：

  ```python 
  days = "Mon Tue Wed Thu Fri Sat Sun"
  months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
  
  print("Here are the days: ", days)
  print("Here are the months: ", months)
  
  print("""There's something going on here.
  With the three double-quotes.
  We'll be able to type as much as we like.
  Even 4 lines if we want, or 5, or 6.
  """)
  
  print(""" "ddddd","ddddddd","ffff" """)
  print("""shjhsjh"ddddd"ddddd""")
  ```
  
* ### 学习内容：`\n`；`"""`(三引号)

  * ### `\n`

    * 换行符
    * `\`是转义的意思

  * ### `"""这里面可以有引号，逗号，换行，空格等都不会报错"""`

    * 允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
    
    * 一对连续的单引号或者双引号（三个单引号或三个双引号）格式如下：
    
      `'''内容'''`；`"""内容"""`
    
      引号之间没有空格。
    
      输入：
    
      ```python
      print("""
      "aaa","bbb",,,,'bbb'"双引号"双引号 \n (ddsds) 回车空行
      回车空行
      """)
      ```
    
      结果：
    
      ```powershell
       "aaa","bbb",,,,'bbb'"双引号"双引号
       (ddsds) 回车空行
      回车空行
      ```
    
      无论是回车换行还是换行符换行都会识别，输出换行

* ### 改变代码（寻找可能情况及错误）

  * #### 在双引号或者单引号中使用回车换行，会报错

    输入：

    ```python
    print("aaa
    回车换行
    ")
    ```
    
    结果：
    
    ```powershell
      File "TEST.py", line 1
        print("aaa
                 ^
    SyntaxError: EOL while scanning string literal
    ```
    
    语法错误：检测到非法结束符。
  

