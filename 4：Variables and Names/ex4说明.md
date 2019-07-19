# EX4: Variables and Names

* 例子：

  ```python
  cars = 100
  space_in_a_car = 4
  drivers = 30
  passengers = 90
  cars_not_driven = cars - drivers
  cars_driven = drivers
  carpool_capacity = cars_driven * space_in_a_car
  average_passengers_per_car = passengers / cars_driven
  
  print("There are", cars,"cars available.")
  print("There are only", drivers,"drivers available.")
  print("There will be", cars_not_driven, "empty cars today.")
  print("We can transport", carpool_capacity,"people today.")
  print("We have", passengers, "to carpool today.")
  print("We need to put about", average_passengers_per_car, "in each car.")
  ```

* 学习内容：变量；`=`；`_`

  * 变量(variable)

    * 变量就是一个存储数据的**内存空间对象**。定义一个变量，即向内存申请一个带地址的访问空间对象，用来存储数据，通过变量名找到（**指向）**这个值。
    * 在`python`中的变量赋值不需要声明类型，即不需要说明这个数据是`int`型，`float`型等。
    * 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

  * `=`

    * 赋值。`a = 1`：将`1`这个数值赋予`a`，`a`为变量名。
    
    * `=` 和 `==` 是有区别的：
    
      1. `=` 的意思是赋值，`==`的意思是比较两边的值是否一致
    
         ```python
         输入：
         cars = 100
         drivers = 30
         print(cars, cars == drivers)
         
         结果：
         100 False
         ```
    
         `cars`的值为100。
    
         `False`：`cars`和`drivers`的值是否相等，结果是`False`，意思是不相等。
    
  * `_`

    * 下划线。
  * 用于变量名中，代替空格。因为如果一个变量里面有空格，会报错。

* 深入练习（Study Drills）

  * 是否有必要用浮点数？

    不清楚，但是使用浮点数能够提高精度，但就现在尝试的计算中是否为浮点数对计算结果没有什么影响。

    输入：

    ```python
    num1 = 100
    num2 = 3
    num3 = 3.0
    
    print(num1 / num2)
    print(num1 / num3)
    ```

    结果：

    ```powershell
    33.333333333333336
    33.333333333333336
    ```

* 破坏代码

  （运行代码太长，只选取部分来执行）

  * 变量名不一致

    输入：
  
    ```python
  space_in_a_car = 4
    drivers = 30
  cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    
    print("We can transport", car_pool_capacity,"people today.")
    ```
  
    结果：
  
  ```powershell
    Traceback (most recent call last):
    File "ex4.py", line 13, in <module>
        print("We can transport", car_pool_capacity,"people today.")
  NameError: name 'car_pool_capacity' is not defined
    ```

    变量名错误：`car_pool_capacity` 没有被定义。
  
    变量名必须完全一致。

  * 同一变量名赋值两次

    输入：
  
    ```python
    space_in_a_car = 4
    # print(space_in_a_car)
  
    space_in_a_car = 5
print("space_in_a_car: ", space_in_a_car)
    ```
  
    结果：
  
    ```powershell
  space_in_a_car:  5
    ```
  
    因为同一变量名，下面的赋值会覆盖上面的赋值。
  
* `print()`中缺了逗号
  
  输入：
  
    ```python
    cars = 100
    print("There are" cars,"cars available.")
    ```
  
    结果：
  
    ```powershell
      File "ex4.py", line 2
        print("There are" cars,"cars available.")
                             ^
    SyntaxError: invalid syntax
  ```
    
  语法错误：无效语法。
    
    如果没有逗号，`print()`在打印输出时遇到右引号时就以为命令已经结束了，就无法识别右引号后面的内容。
    
  * 
  
  * 运算式可以在`print()`中执行
  
    输入：
  
    ```python 
    drivers = 30
    passengers = 90
    cars_driven = drivers
  average_passengers_per_car = passengers / cars_driven
    
  print("We need to put about", average_passengers_per_car, "in each car.")
    print("We need to put about", passengers / cars_driven, "in each car.")
    ```
    
    结果：
    
    ```powershell
    We need to put about 3.0 in each car.
  We need to put about 3.0 in each car.
    ```
    
    上下两个`print()`函数的内容等价。
    
    
    
    



