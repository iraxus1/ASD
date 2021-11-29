import time
from random import randint


def bubblesort(A):
    for i in range(len(A) - 1):
        for j in range(0 , len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def bubblesortreverse(A):
    for i in range(len(A) - 1):
        for j in range(0 , len(A) - i - 1):
            if A[j] < A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


A = []
for i in range(100000):
    A.append(randint(1, 1000))


start = time.time()
bubblesort(A)
end = time.time()
print("sortowanie losowych: ", end - start)
start1 = time.time()
bubblesort(A)
end1 = time.time()
print("sortowanie posortowanych od najmniejszej liczby do najwiekszej: ", end1 - start1)
bubblesortreverse(A)
start2 = time.time()
bubblesort(A)
end2 = time.time()
print("sortowanie posortowanych odwrotnie: ", end2 - start2)