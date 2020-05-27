import random
from timeit import default_timer as timer

start = timer()

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]#j becomes the key
        i = j - 1 #i becomes one less then key
        while i >= 0 and key < A[i]:
                A[i + 1] = A[i]#shift right
                i -= 1
        A[i + 1] = key

def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res

num = 60000
start = 1
end = 500000
randnums = (Rand(start, end, num))
insertionSort(randnums)
for i in range(len(randnums)):
    print ("%d" %randnums[i])

elapsed_time = timer() - start
print(elapsed_time)
