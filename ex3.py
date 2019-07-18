print("I will now count my chickens:")

print("Hens",25.0 + 31.0 / 6.0) # 先做除法运算，再做加法运算
print("Roosters",100 - 25 * 3 % 4) # 25*3%4意思为取余，取余值为3，所以得数为97

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6) # 先计算4%2，为0,1/4, 为0.25，在计算加减法

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7) # 比较大小，先运算后比较大小，若比较成立则为true，若比较不成立则为false

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > --6 , --6) # python不存在自增自减，++i/--i的意思为正负关系，正正得正，负负得正，++i/--i=i
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
