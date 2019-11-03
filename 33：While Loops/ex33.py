def loop(loop_num, increment):
    i = 0
    numbers = []
    while i < loop_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

loopn = eval(input(">>>"))
incre = eval(input(">>>"))
loop(loopn, incre)

# loopn, incre = map(eval, input(">>>").split(" "))
# loop(loopn, incre)

# num = input(">>>").split(" ")
# loop(eval(num[0]), eval(num[1]))

# num = [eval(x) for x in input(">>>").split(" ")]
# loop(*num)

for num in numbers:
    print(num)

# def loop(loop_num, increment):
#     i = 0
#     numbers = []
#     for i in range(0, loop_num + 1):
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         # i = i + increment
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")