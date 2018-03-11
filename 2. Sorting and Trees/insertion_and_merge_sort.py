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

def merge_sort(L):
    if len(L) > 1:
        q = len(L)//2
        left = merge_sort(L[:q])
        right = merge_sort(L[q:])
        return merge(left,right)
    return L
def merge(left,right):
    A = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A.append(left[i])
            i += 1
        else:
            A.append(right[j])
            j += 1
    A += left[i:] #If two lists are of different length, the while loop stops when the elements in the shorter
    A += right[j:] #list are all appended. Therefore, we need to append whatever is left in the longer list.
    return A

def new_merge(lst):
    if len(lst)>1:
        cut = int(len(lst)/2)
        left = new_merge(lst[:cut])
        right = new_merge(lst[cut:])
        return new_mergesort(left, right)
    return lst
def new_mergesort(left, right):
    final = []
    l = 0
    r = 0
    status = True
    while status:
        if left[l] <= right[r]:
            final.append(left[l])
            l += 1
            if l == len(left):
                status = False

        else:
            final.append(right[r])
            r += 1
            if r == len(right):
                status = False
    final += left[l:]
    final +=right[r:]
    return final

print(new_merge(sample1))