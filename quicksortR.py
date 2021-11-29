from random import randint


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
for i in range(1000000):
    A.append(randint(1, 10000))
quicksortreverse(A, 0, len(A) - 1)