sample1 = [34, 21, 93, 14, 71, 31, 44, 52, 20]
sample2 = [11, 26, 33, 7, 43, 1, 4, 35, 80]

def insertionSort(lst):
    for n in range(len(lst)-1):
        index = n + 1
        while lst[index] < lst[index-1] and index != 0:
            swap = lst[index-1]
            lst[index-1] = lst[index]
            lst[index] = swap
            index -= 1
    return lst

import numpy as np          
def mergesort(lst):
    n = len(lst)
    lst = np.asarray(lst).reshape(n,1)
    if n%2 == 1:
        extra = lst[-1]
        lst = np.delete(lst, -1)
        lst = lst.reshape(int(n/2), 2)
        lst = np.append(lst, extra)
    else:
        lst = lst.reshape(int(n/2), 2)


    return lst
