inp = open("input1a.txt", mode='r')
data = inp.readlines()
temp = data[0].split()
arr = list(map(int, temp[2:]))
def partition(arr, low, high):
    # pivot (Element to be placed at right position)
    pivot = arr[high]
    i = low - 1  # Index of smaller element and indicates the
    # right position of pivot found so far
    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i += 1  # increment index of smaller element
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def findK(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        idx = partition(arr, low, high)
        if idx == k - 1:
            return arr[idx]
        elif idx > k - 1:
            high = idx - 1
        else:
            low = idx + 1
for i in range(1, len(data)):
    var = data[i].strip()
    print(findK(arr, int(var[-1])))
inp.close()