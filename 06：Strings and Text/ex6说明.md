# EX6: Strings and Text

* ### 例子：

  ```python
  # 给 types_of_people 赋值：10
  types_of_people = 10
  # 将字符串赋值给 x ，使用 f-string 将 type_of_people 嵌入 x 中
  x = f"There are {types_of_people} types of people."
  
  # 赋值
  binary = "binary"
  do_not = "don't"
  # 赋值并嵌入
  y = f"Those who know {binary} and those who {do_not}."
  
  # 打印输出
  print(x)
  print(y)
  
  # 插入变量值打印输出
  print(f"I said: {x}")
  print(f"I also said: '{y}'")
  
  # 赋值
  hilarious = False
  joke_evaluation = "Isn't that joke so funny?! {}"
  
  print(joke_evaluation.format(hilarious))
  
  w = "This is the left side of..."
  e = "a string with a right side."
  
  # 连接两个字符串组成更长的字符串
  print(w + e)
  ```

* ### 学习内容：`f`；`format`；用`print`进行debug

  * #### `f`

    * 变量字符串格式化输出，将变量值融入句子中成为新的字符串输出
    * 会将变量值类型转化为字符串输出
    * `f`不能嵌套
    * 开头例子表明，`f`创建的新字符串可以赋值给变量
    
  * #### `.format()`

    * 格式化字符串的函数 **str.format()**，它增强了字符串格式化的功能

    * `f` 和`.format()`大部分时候可以互换

      输入：

      ```python
      hilarious = False
      joke_evaluation1 = "Isn't that joke so funny?! {}"
      joke_evaluation2 = "Isn't that joke so funny?! {}"
      
      print(joke_evaluation1.format(hilarious))
      print(joke_evaluation2 + f"{hilarious}")
      print(f"{joke_evaluation2}" + f"{hilarious}")
      print(f"{joke_evaluation2}{hilarious}")
      ```
      
      结果：
      
      ```txt
      Isn't that joke so funny?! False
      Isn't that joke so funny?! False
      Isn't that joke so funny?! False
      Isn't that joke so funny?! False
      ```
      
      从结果可以看出，`f`本身就能够存在很多种表达方式，且能与`.format()`进行互换。
    
  * #### 用`print`进行debug

    * 找到可能出错的地方，可以在错误前一行和后一行用`print`输出，判断是否出错，或者是弄明白某段代码的含义。

    * 比如为了弄明白变量x的赋值内容：

      输入：

      ```python
      types_of_people = 10
      x = f"There are {types_of_people} types of people."
      
      binary = "binary"
      do_not = "don't"
      y1 = "Those who know {binary} and those who {do_not}."
      
      print(">>>> after assign y : ", y1)
      print(x)
      print(">>>> before print y : ", y1)
      print(y1)
      ```

      结果：

      ```powershell
      >>>> after assign y :  Those who know {binary} and those who {do_not}.
      There are 10 types of people.
      >>>> before print y :  Those who know {binary} and those who {do_not}.
      Those who know {binary} and those who {do_not}.
      ```

      从结果可以看出y变量少了什么（等号后面应该还有一个f）

      

* ### 深入练习（Study Drills）

  * #### 我认为共有3个地方是字符串套字符串的

    ```python
    y = f"Those who know {binary} and those who {do_not}."
    print(f"I said: {x}")
    print(f"I also said: '{y}'")
    ```
    
    以下两个不是
    
    ```python
    x = f"There are {types_of_people} types of people."
    print(joke_evaluation.format(hilarious))
    ```
    
    原因是，下面的两条命令中，第一条是在字符串中嵌套了数值类型变量，第二条是字符串中嵌套了Boolean类型变量（true/false）。
  
* ### 改变代码（寻找可能情况及错误）

  * #### 不同类型的数据不能用`+`连接
    
    输入：

    ```python
    hilarious = False
    joke_evaluation2 = "Isn't that joke so funny?! {}"
    
    print(f"{joke_evaluation2 + hilarious}")
    ```
    
    结果：
    
    ```powershell
    Traceback (most recent call last):
      File "TEST.py", line 4, in <module>
        print(f"{joke_evaluation2 + hilarious}")
    TypeError: can only concatenate str (not "bool") to str
    ```
    
    类型错误：只能连接同类型的变量值。

  * #### 单引号和双引号的混合使用
  
    输入：
  
    ```python
    print("把'单引号'放进双引号中")
    print('把"双引号"放进单引号中')
    print("把"另外双引号"放进双引号中")
    print('把'另外单引号'放进单引号中')
    ```
    
    结果：
    
    ```txt
    把'单引号'放进双引号中
    把"双引号"放进单引号中
    
      File "TEST.py", line 3
        print("把"另外双引号"放进双引号中")
                     ^
    SyntaxError: invalid syntax
    
      File "TEST.py", line 4
        print('把'另外单引号'放进单引号中')
                     ^
    SyntaxError: invalid syntax
    ```
    
    从结果可以得知单引号和双引号可以混合使用，但是单引号中不可存在另外的单引号，双引号中不能存在另外的双引号。（以上结果为结果的合并，想要测试此错误要要分开测试）

