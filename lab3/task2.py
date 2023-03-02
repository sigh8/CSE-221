inp = open("input2.txt", mode='r')
data = inp.readlines()
heap = list(map(int, data[0].split()))


def heapify(arr, size, i):
    small = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < size and arr[l] < arr[small]:
        small = l
    if r < size and arr[r] < arr[small]:
        small = r
    if small != i:
        arr[i], arr[small] = arr[small], arr[i]
        heapify(arr, size, small)


def build(inp):
    for i in range(len(inp) // 2 - 1, -1, -1):
        heapify(inp, len(inp), i)


def swim_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def add(heap, val):
    heap.append(val)
    swim_up(heap, len(heap) - 1)


def sink(heap, i):
    l = 2 * i + 1
    r = 2 * i + 2
    small = i
    if l < len(heap) and heap[l] < heap[small]:
        small = l
    if r < len(heap) and heap[r] < heap[small]:
        small = r
    if small != i:
        heap[i], heap[small] = heap[small], heap[i]
        sink(heap, small)


def delete(heap):
    if len(heap) == 0:
        return None
    heap[0], heap[-1] = heap[-1], heap[0]
    small = heap.pop()
    sink(heap, 0)
    return small


def heapSort(heap):
    sortedHeap = []
    while len(heap) > 0:
        sortedHeap.append(delete(heap))
    return sortedHeap

build(heap)

while True:
    usr = input("Please enter command: ")
    if usr == "a" or usr == "A":
        val = int(input("Please enter value: "))
        add(heap, val)
        print(f"Added: {val} \nCurrent heap: {heap}")
    elif usr == "b" or usr == "B":
        print(f"Deleted: {delete(heap)} \nCurrent heap: {heap}")
    elif usr == "s" or usr == "S":
        print(f"Sorted heap: {heapSort(heap)}")
    elif usr == "q" or usr == "Q":
        break

inp.close()