import sys
import time
from random import randint
sys.setrecursionlimit(100000)


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksortreverse(A, p, r):
    if p < r:
        q = partitionreverse(A, p, r)
        quicksortreverse(A, p, q - 1)
        quicksortreverse(A, q + 1, r)


def partitionreverse(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


A = []
for i in range(100000):
    A.append(randint(1, 1000))

start = time.time()
quicksort(A, 0, len(A) - 1)
end = time.time()
print("sortowanie losowych: ", end - start)
start1 = time.time()
quicksort(A, 0, len(A) - 1)
end1 = time.time()
print("sortowanie posortowanych od najmniejszej liczby do najwiekszej: ", end1 - start1)
quicksortreverse(A, 0, len(A) - 1)
start2 = time.time()
quicksort(A, 0, len(A) - 1)
end2 = time.time()
print("sortowanie posortowanych odwrotnie: ", end2 - start2)