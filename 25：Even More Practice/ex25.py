def break_words(stuff):
    """This function will break up wprds for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# a = 'h e l l o'
# b = 'hope you can enjoy the learning time'
# c = break_words(a)
# # 函数中有print，不需要用print调用并输出；函数中无print，用print才能使得return的内容输出。
# print(c) 
# print(sort_words(c))
# print_first_word(c)
# print_last_word(c)
# print(sort_sentence(b))
# print_first_and_last(b)
# print_first_and_last_sorted(b)