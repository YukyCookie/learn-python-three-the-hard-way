print("""让我们来玩个随机数的游戏吧！
请输入0至100以内的任意一个数字""")

num = eval(input("> "))
if type(num) == int or type(num) == float:
    if 0 <= num <= 10 :
        print("恭喜你，获得10000元。")
        print("请问是否要继续游戏？输入1表示继续，输入0表示结束游戏。")

        game_num = input("> ")

        if game_num == "1":
            print("恭喜，你被抢了5000元。")
            print(" 请问是否想要追回损失的钱？输入1表示想要追回，输入0表示就此放弃。")

            get_money_back = input("> ")

            if get_money_back == "1":
                print("勇气可嘉，但是非常遗憾，你剩下的钱也被抢光了。")
            elif get_money_back == "0":
                print("恭喜你，你用这仅有的5000元发家致富，成为了全球首富。")
            else:
                print("因为不做决定，系统决定再奖励你10000000000元。")
                
        elif game_num == "0":
            print("结束游戏，你一共获得了10000元。")

        else:
            print("没有得到明确地指示，所以系统把你变成了游戏中的路人甲。")

    # 以下两种表示范围的方式有差别，11 <= num <= 90能够识别浮点数，num in range(11,91)不可以。
    # elif 11 <= num <= 90:
    elif num in range(11,91):
        print("恭喜你，成功进入系统，成为一名普通玩家。")
        print("是否想要得到秘籍，成为顶级玩家，统治系统。")
        print("输入1表示希望得到，输入其他表示你愿意自己靠自己的努力升级打怪")

        get_num = input("> ")

        if get_num == "1":
            print("秘籍已得，秘籍说，顶级玩家可以通过大量氪金实现。")

        else:
            print("你的上进心，系统看见了，所以系统决定助你一臂之力。恭喜你，成为了顶级玩家。")


    # elif 91 <= num <= 100:
    elif num in range(91,101):
        print("恭喜你，获得了一个游戏账号。")

    else:
        print("因为你的数字输入不符范围，所以决定由你来继承系统，为玩家设置无限障碍。")

else:
    print("请输入正确的数字类型")