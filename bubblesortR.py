from random import randint


def bubblesortreverse(A):
    for i in range(len(A) - 1):
        for j in range(0 , len(A) - i - 1):
            if A[j] < A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


A = []
for i in range(1000000):
    A.append(randint(1, 1000))
bubblesortreverse(A)