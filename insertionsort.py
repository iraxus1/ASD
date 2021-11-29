import time
from random import randint


def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


def insertionsortreverse(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


A = []
for i in range(100000):
    A.append(randint(1, 1000))
start = time.time()
insertionsort(A)
end = time.time()
print("sortowanie losowych: ", end - start)
start1 = time.time()
insertionsort(A)
end1 = time.time()
print("sortowanie posortowanych od najmniejszej liczby do najwiekszej: ", end1 - start1)
insertionsortreverse(A)
start2 = time.time()
insertionsort(A)
end2 = time.time()
print("sortowanie posortowanych odwrotnie: ", end2 - start2)