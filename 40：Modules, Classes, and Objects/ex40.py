class Song(object):
    def __init__(self, lyrics):
        # print(">>>> lyrics", lyrics)
        print(">>>> self", self)
        self.lyrics = lyrics
        # print(">>>> self.lyrics", self.lyrics)
    
    def sing_me_a_song(self):
        print(">>>> begin")
        for line in self.lyrics:
            print(line)

# 只会执行__init__() 
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
# print(">>>> happy_bday", happy_bday)
# print(">>>> happy_bday.lyrics", happy_bday.lyrics)

print("-" * 30)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
# print(">>>> bulls_on_parade", bulls_on_parade)
# print(">>>> bulls_on_parade.lyrics", bulls_on_parade.lyrics)

# 执行sing_me_a_song()
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()