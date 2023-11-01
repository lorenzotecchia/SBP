def HeapSort(A, n):
    BuildHeap(A, n)
    for i=n-1 in range(1):
        Swap(A, 0, i)
        Heapify(A, i , 0)

def BuildHeap(A, n):
    for i = ((n/2) - 1) in range(0):
        Heapify(A, n, i)

:w

