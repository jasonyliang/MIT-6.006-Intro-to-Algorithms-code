'''
Identify a heap: a data structure visualized in a tree with either heap max or heap min property

'''

def is_max_heap(lst):
    '''
    identify whether a given list is a max heap
    '''
    heap = True
    for n in range(int(len(lst)/2)):
        if lst[2*n] <= lst[n] and lst[2*n+1] <= lst[n]:
            heap = True
        else:
            return False
    return heap
