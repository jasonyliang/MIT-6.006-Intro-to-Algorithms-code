'''
Inspiration from https://brilliant.org/wiki/rabin-karp-algorithm/#complexity-of-rabin-karp

'''
class Hashfunction:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord
        
        # create rolling hash
        for i in range(sizeWord):
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))
        
        # indexing
        self.window_start = 0
        # end of index
        self.window_end = sizeWord
    def move_window(self):
        if self.window_end <= len(self.text)-1:
            # remove left letter of the string
            self.hash -= (ord(self.text[self.window_start]) - ord("a") + 1) * 26 ** (self.sizeWord - 1)
            self.hash *= 26 # every other term increases but an order of 1 for the constant 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1 # last term
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabinkarp(word, text):
    if word == '' or text == '':
        return None
    if len(word) > len(text):
        return None

    texthash = Hashfunction(text, len(word))
    wordhash = Hashfunction(word, len(word))
    # wordhash.move_window()

    for i in range(len(text) - len(word) + 1):
        if texthash.hash == wordhash.hash:
            if texthash.window_text() == word:
                return i
        texthash.move_window()
    return None
