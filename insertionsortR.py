from random import randint


def insertionsortreverse(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


A = []
for i in range(1000000):
    A.append(randint(1, 1000))
insertionsort(A)

print(A)