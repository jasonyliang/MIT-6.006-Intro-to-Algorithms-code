'''
Inspiration from https://brilliant.org/wiki/rabin-karp-algorithm/#complexity-of-rabin-karp

'''
class Hashfunction:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord
        

