# EX5: More Variables and Printing

* ### 例子：

  ```python
  my_name = 'Zed A. Shaw'
  my_age = 35 # not a lie
  my_height = 74 # inches
  my_weight = 180 # lbs
  my_eyes = 'Blue'
  my_teeth = 'White'
  my_hair = 'Brown'
  
  print(f"Let's talk about {my_name}.")
  print(f"He's {my_height} centimeters tall.")
  print(f"He's {my_weight} kilograms heavy.")
  print(f"Actually that's not too heavy.")
  print(f"He's got {my_eyes} eyes and {my_hair} hair.")
  print(f"His teeth are usually {my_teeth} depending on the coffee.")
  
  # this line is tricky, try to get it exactly right
  total = my_age + my_height + my_weight
  print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
  ```

* ### 学习内容：`f`；`+`；`round()`

  * #### `f`

    * 变量字符串格式化输出，将变量值融入句子中成为新的字符串输出
    * 会将变量值类型转化为字符串输出
    
    * `f`不能嵌套
  * #### `+`

    * 加法运算；连接字符串
    
      输入：
    
      ```python
      a = 1
      b = 2
      c = "hello"
      d = "world"
      
      print("a + b = ", a + b)
      print("c + d = ", c + d)
      ```
    
      结果：
    
      ```txt
      a + b =  3
      c + d =  helloworld
      ```
    
      注意：不能将数字与字符串用 `+` 相连，会报错。

  * #### `round()`
    
    * 四舍五入取整
    * `print(round(1.777))` 输出 `2`

* ### 深入练习（Study Drills）

  * #### 去掉变量名中的`my_`，将数据转化为厘米和千克，并取整

    输入：

    ```python
    name = 'Zed A. Shaw'
    age = 35 # not a lie
    height = 2.54 * 74 # inches
    weight = 0.4535924 * 180 # lbs
    eyes = 'Blue'
    teeth = 'White'
    hair = 'Brown'
    
    print(f"Let's talk about {name}.")
    print(f"He's {round(height)} centimeters tall.")
    print(f"He's {round(weight)} kilograms heavy.")
    print(f"Actually that's not too heavy.")
    print(f"He's got {eyes} eyes and {hair} hair.")
    print(f"His teeth are usually {teeth} depending on the coffee.")
    
    # this line is tricky, try to get it exactly right
    total = age + height + weight
    print(f"If I add {age}, {height}, and {weight} I get {total}.")
    ```

    结果：

    ```txt
    Let's talk about Zed A. Shaw.
    He's 188 centimeters tall.
    He's 82 kilograms heavy.
    Actually that's not too heavy.
    He's got Blue eyes and Brown hair.
    His teeth are usually White depending on the coffee.
    If I add 35, 187.96, and 81.646632 I get 304.606632.
    ```

    `round(height)`会对`height`的数值四舍五入取整，188

    `height`直接输出的为计算结果值，187.96

* ### 破坏代码（下面为错误情况及运行结果）

  * #### `f`嵌套

    输入：

    ```python
    my_age = 35 # not a lie
    my_height = 74 # inches
  my_weight = 180 # lbs
    
  print(f"{my_height}, f"{my_age}"")
    
    ```
  
    结果：
  
    ```txt
    File "ex5.py", line 20
      print(f"{my_height}, f"{my_age}"")
                               ^
  SyntaxError: invalid syntax
    ```

    语法错误：无效语法。

  * #### 字符串与数值变量或数字用`+`相连接
  
    输入：

    ```python
  my_name = 'zed'
    my_eyes = 'blue'
    my_height = 74 
    my_weight = 180 
    
    print(f"{my_height + my_weight}")
    print(f"{my_height} + {my_weight}")
    print(f"{my_name + my_eyes}")
  print(f"{my_name} + {my_eyes}")
    ```

    结果：

    ```txt
  254
    74 + 180
    zedblue
    zed + blue
    ```

    



