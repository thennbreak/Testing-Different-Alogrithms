import random
from timeit import default_timer as timer

start = timer()

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1)#Left half
    R = [0] * (n2)#Right half

    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    i = 0#index of first subarray
    j = 0#index of second subarray
    k = p#index of merged subarray
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + (r-1)) // 2#floor division to elimate float types
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res

num = 60000
start = 1
end = 500000
arr = (Rand(start, end, num))
n = len(arr)

mergeSort(arr, 0, n-1)
for i in range(n):
    print ("%d" %arr[i])

elapsed_time = timer() - start
print(elapsed_time)
