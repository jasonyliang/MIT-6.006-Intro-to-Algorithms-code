'''
Identify a heap: a data structure visualized in a tree with either heap max or heap min property

'''
import heapq
x = [0, 1, 3,4,2,1,3]
heapq.heapify(x)
def is_min_heap(lst):
    '''
    identify whether a given list is a min heap
    '''
    heap = True
    for n in range(1,int(len(lst)/2)+1):
        if lst[2*n-1] >= lst[n-1] and lst[2*n-1] >= lst[n-1]:
            heap = True
        else:
            return False
    return heap
print(x)
print(is_min_heap(x))

def heapify(lst, n, i):
    '''
    lst is the list to be sorted
    n is the length the of list
    i is the parent node concerned
    '''
    parent = i
    left = 2*i + 1
    right = (2*i + 1) + 1
    if left < n and lst[left] > arr[i]:
        parent = left
    if right < n and lst[right] > arr[largest]:
        parent = right

    if parent != i:
        lst[i], lst[parent] = lst[parent], lst[i]
        heapify(lst, n, parent) #heapify the root since we switched it

    

