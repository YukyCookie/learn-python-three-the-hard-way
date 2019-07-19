# EX3: Numbers and Math

* 例子：

  ```python 
  print("I will now count my chickens:")
  
  print("Hens",25 + 31 / 6) 
  print("Roosters",100 - 25 * 3 % 4) 
  
  print("Now I will count the eggs:")
  
  print(3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6) 
  
  print("Is it true that 3 + 2 < 5 - 7?")
  
  print(3 + 2 < 5 - 7) 
  
  print("What is 3 + 2?", 3 + 2)
  print("What is 5 - 7?", 5 - 7)
  
  print("Oh, that's why it's False.")
  
  print("How about some more.")
  
  print("Is it greater?", 5 > -2) 
  print("Is it greater or equal?", 5 >= -2)
  print("Is it less or equal?", 5 <= -2)
  ```

  

* 学习内容：+、-、/、*、%、<、>、<=、>=

  * 加、减、除、乘、取余、小于、大于、小于等于、大于等于

  * %：取余，取值：X除与Y所得到的余数。（意义不是百分号）

    ​		比如：100 / 16 = 6 ······ 4 等价于 100 % 16 = 4

* 深入练习（Study Drills）

  * 浮点数更精确（带小数的为浮点数）

* 破坏代码

  * `++i/--i`

    输入：

    ```python
    print("Is it greater?", 5 > --6 , --6) 
    print("Is it greater?", 5 > -6, -6)
  print("Is it greater?", 5 > --2 , --2)
    print("Is it greater?", 5 > -2 , -2)
    ```
  ```
  
    `print`的最后一项是为了验证`--i`和`-i`输出的数值，可以去掉。
  
    结果：
  
    ```powershell
    PS F:\python\hard way 练习> python ex3.py
  Is it greater? False 6
    Is it greater? True -6
  Is it greater? True 2
    Is it greater? True -2
  ```
  
  1. 不会报错，但是`python`没有`++`和`--`。
    2. 从以上结果可以看出，`--6`和`--2`在`python`中是`6`和`2`。
    3. 有时候在 Python 中看到存在 `++i` 这种形式，这其实不是自增，只是简单的表示正负数的符号而已。正正得正，负负得正，所以 `++i` 和 `--i` 都是 `i` 。
    4. `python`自增自减的表达为：`a = a + 1` 或 `a += 1  `



`++i`和`--i`参考链接：[1](https://blog.csdn.net/u011236348/article/details/89311490)，[2](https://blog.csdn.net/guang09080908/article/details/47273765)







