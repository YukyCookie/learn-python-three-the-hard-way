import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# ‘%%%’表示类名，‘@@@’表示参数（可以有多个），‘***’表示函数名，变量名，赋值
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, @@@)":
      "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef *** (self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# 如果没有设定sys.argv的参数个数，那么argv的参数个数可以为任意个数
# 如果输入python ex41.py english，则PHRASE_FIRST = True，反之为False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# 将网页中内容下载并按行读取，并将每行赋值于变量word
for word in urlopen(WORD_URL).readlines():
    # 将变量word每次赋值内容去掉换行符，转换为str类型，添加到WORDS列表
    WORDS.append(str(word.strip(), encoding="utf-8"))

# 设定函数，处理键snippet和值phrase
def convert(snippet, phrase):
    # 统计‘%%%’的数量，从WORDS中随机选取该数量的元素，将每个元素的首字母大写，以列表形式储存，赋值于class_names
    # class_names的整个形式为列表推导式
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    # 统计‘***’的数量，从WORDS中随机选取该数量的元素，以列表形式返回，赋值于other_names
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # 键snippet中可以有多个‘@@@’，所以用循环
    for i in range(0, snippet.count("@@@")):
        # ‘@@@’表示参数，参数可以有多个，所以参数数量随机，1-3个
        param_count = random.randint(1,3)
        # 从WORDS中随机选取param_count数量的元素，以‘，’连接生成一个新的字符串，添加到param_names列表中
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    #  循环两次，第一次snippet，第二次phrase
    for sentence in snippet, phrase:
        # 切片复制sentence给result，但是不清楚为什么需要用到切片，这里的sentence是字符串不是列表。
        result = sentence[:]

        # fake class names
        # 用class_names中存储的名称替换result中的‘%%%’，最多替换1次
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        # 用other_names中存储的名称替换result中的‘***’，最多替换1次
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        # 用param_names中存储的名称替换result中的‘@@@’，最多替换1次
        for word in param_names:
            result = result.replace("@@@", word, 1)

        # 将替换好的result放入results列表中
        results.append(result)

    # 两次循环后，results中以列表形式储存着处理好的键和值，返回处理好的键值列表
    return results

# keep going until they hit CTRL-D
try:
    # 无限循环抽取题目
    while True:
        # 将字典PHRASES的键以列表形式赋予变量snippets
        snippets = list(PHRASES.keys())
        # 打乱snippets中元素的顺序
        random.shuffle(snippets)

        # 遍历snippets列表，抽题
        for snippet in snippets:
            # 将键snippet在字典PHTASES中对应的值赋予phrase
            phrase = PHRASES[snippet]
            # 将函数convert()的返回值赋予变量question和answer，返回的是键值列表，列表第一项给question，第二项给answer
            question, answer = convert(snippet, phrase)
            # 如果PHRASE_FIRST = True，即输入python ex41.py english，将question和answer的内容互换
            # 互换目的是，给出英文写出相应的表达式
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
# 会抛出异常，EORError为读不到数据，KeyBoardInterrupt为通常由ctrl+c或者Delete抛出的异常
except EOFError:
    print("\nBue")