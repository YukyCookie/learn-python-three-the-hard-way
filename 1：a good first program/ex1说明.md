# EX1: A Good First Program

* 例子：

  ```python
  print("Hello World!")
  print("Hello Again")
  print("I Like Type This.")
  print("This is fun!")
  print('Yay!Printing')
  print("I'd much rather you 'not'.")
  print('I "said" do not touch this')
  print("I should word hard to get a job")
  ```

* 学习内容：`print()`；`#`；

  * `print()`

    * 用于打印输出

    * 在 python 3.x 中，`print()`有括号

      1. 格式：`print("需要输出的内容写在这里面")`

         ​			`print('单引号也可以用在字符串上')`

      2. 注意：在 python 2.x 中，`print`是没有括号的，这是因为它还不是一个函数，只是一个关键字
      
    * 一条`print`命令执行结束，会默认自动换行。

  * `# 在这后面写下想要解释的内容或者不想运行的代码`

    * 注释
    * 不会运行，就是解释作用
    * 快捷键：`ctrl + /`
      1. 只要将光标放到你要写入注释的那一行，按`ctrl + /`，那一行就会成为注释
      2. 如果想要取消注释，选中要取消注释的行，按`ctrl + /`，注释就会取消
      3. 是否为注释，就看行前面有没有`#`

* 深入练习（Study Drills）

  * 模仿

    ```python
    print("make another line")
    ```

  * 只显示一行

    ```python
    print("Hello World!")
    # print("Hello Again")
    # print("I Like Type This.")
    # print("This is fun!")
    # print('Yay!Printing')
    # print("I'd much rather you 'not'.")
    # print('I "said" do not touch this')
    # print("I should word hard to get a job")
    ```

* 破坏代码（下面为错误情况及运行结果）

  * `print`

    输入：

    ```python
    print "Hello World"
    ```

    结果：

    ```powershell
    PS F:\python\hard way 练习> python ex1.py
      File "ex1.py", line 1
        print "Hello World!"
                           ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?
    ```

    语法错误：调用`print`时缺少括号。

  * `print(`

    输入：

    ```python
    print("Hello World!"
    ```

    结果：

    ```powershell
    PS F:\python\hard way 练习> python ex1.py
      File "ex1.py", line 10
    
        ^
    SyntaxError: unexpected EOF while parsing
    ```

    

  * `print("`

    输入：

    ```python
    print("Hello World!
    print("Hello World!)
    ```

    结果：

    ```powershell
    PS F:\python\hard way 练习> python ex1.py
      File "ex1.py", line 1
        print("Hello World!
                          ^
    SyntaxError: EOL while scanning string literal
    
    PS F:\python\hard way 练习> python ex1.py
      File "ex1.py", line 1
        print("Hello World!)
                           ^
    SyntaxError: EOL while scanning string literal
    ```

    语法错误：检测到非法结束符。

  * 在代码开始输入空格
  
    输入：
  
    ```python 
     print("Hello World!")
    # 前面有个空格
    ```
  
    结果：
  
    ```powershell
    PS F:\python\hard way 练习> python ex1.py
      File "ex1.py", line 1
        print("Hello World!")
        ^
    IndentationError: unexpected indent
    ```
  
    缩进错误：意外缩进。



