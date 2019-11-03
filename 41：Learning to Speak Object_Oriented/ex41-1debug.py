import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

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

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

snippets = list(PHRASES.keys())
print(">>>> snippets: ", snippets)
print("")
random.shuffle(snippets)
print(">>>> snippets/打乱顺序: ", snippets)

for snippet in snippets:
    phrase = PHRASES[snippet]

print(">>>> snippet: ", snippet)
print(">>>> phrase: ", phrase)
print("")

class_names = [w.capitalize() for w in
               random.sample(WORDS, snippet.count("%%%"))]
print(">>>> class_names: ", class_names)
other_names = random.sample(WORDS, snippet.count("***"))
print(">>>> other_names: ", other_names)
results = []
param_names = []

print(">>>> before param_names: ", param_names)
for i in range(0, snippet.count("@@@")):
    param_count = random.randint(1,3)
    print(">>>> 循环赋值前param_names: ", param_names)
    param_names.append(', '.join(
        random.sample(WORDS, param_count)))
    print(">>>> 循环赋值后param_names: ", param_names)

print(">>>> after param_names: ", param_names)

for sentence in snippet, phrase:
    print("")
    print(">>>>>>>>>>>>>> sentence: ", sentence)
    result = sentence[:]
    print(">>>> result/sentence: ", result)

    # fake class names
    print(">>>> 替换%%%: ")
    for word in class_names:
        print(">>>> before result/classnames: ", result)
        result = result.replace("%%%", word, 1)
        print(">>>> after result/classnames: ", result)
    # fake other names
    print(">>>> 替换***: ")
    for word in other_names:
        print(">>>> before result/othernames: ", result)
        result = result.replace("***", word, 1)
        print(">>>> after result/othernames: ", result)

    # fake parameter lists
    print(">>>> 替换@@@: ")
    for word in param_names:
        print(">>>> before result/paramnames: ", result)
        result = result.replace("@@@", word, 1)
        print(">>>> after result/paramnames: ", result)

    results.append(result)
    print(">>>> 循环中results: ", results)

print("")
print(">>>> 循环后results: ", results)
question, answer = results
if PHRASE_FIRST:
    question, answer = answer, question

print(question)
input("> ")
print(f"ANSWER: {answer}\n\n")
