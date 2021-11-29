from random import randint


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapify(A, n, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and A[l] < A[i]:
        largest = l
    if r < n and A[r] < A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def heapsort(A):
    for i in range(len(A) // 2 - 1, -1, -1):
        heapify(A, len(A), i)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


A = []
for i in range(1000000):
    A.append(randint(1, 1000))
heapsort(A)

print(A)
