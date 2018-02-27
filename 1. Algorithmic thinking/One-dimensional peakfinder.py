'''
Given an array:
[a, b, c, d, e, f, g, h, i]
a ~ i are numbers
Position 2 is a peak if and only if 
b >= a and b >= c
Position 9 is a peak iff i >= h
'''
array = [1, 2, 4, 3, 2,5, 4, 1, 1]
#straightforward solution
def peakfinder1(arr):
    n = len(arr)
    for i in range(n):
        if i > 0 and i < n - 1:
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                print("Position ", i + 1, "is a peak")
        elif i == 0:
            if arr[i] >= arr[i + 1]:
                print("Position 1 is a peak")
        else:
            if arr[i] >= arr[i - 1]:
                print("Position ", i + 1, "is a peak")


peakfinder1(array)

#Divide and Conquer (only need to find 'a' peak)
def peakfinder2(arr):
    mid = round(len(arr)/2)
    if mid > 2 and arr[mid] < arr[mid-1]:
        peakfinder2(arr[:mid-1])
    elif mid > 2 and arr[mid] < arr[mid + 1]:
        peakfinder2(arr[mid + 1:])
    else:
        print("Position ", mid + 1, "is a peak")

peakfinder2(array)