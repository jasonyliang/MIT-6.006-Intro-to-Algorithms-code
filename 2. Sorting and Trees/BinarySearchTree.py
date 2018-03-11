'''
Turn a list into a binary search tree structure.
'''
import numpy as np
sample = [30, 17, 40, 14, 20, 46]
sample1 = [49, 46, 41, 39, 12]

class bst():
    def __init__(self, lst):
        h1 = 1
        small = lst[0]
        h2 = 1
        big = lst[0]
        for n in lst:
            if small > n:
                h1 += 1
                small = n
            elif big < n:
                h2 += 1
                big = n
        self.height = max(h1, h2)
    class node():
        def __init__(self, value):
            self.left = False
            self.right = False

    def emptytree(self):
        max_node = 0
        for n in range(self.height):
            max_node += 2**n
        btree = np.zeros(max_node)
        return btree
    def left(self, a, b):
        if lst[b] < btree[a]:
            btree[2*a] = lst[b]
    def right(self, a, b):
        if lst[b] > btree[a]:
            btree[2*a + 1] = lst[b]
    

            
tree = bst(sample)
print(tree.emptytree())





