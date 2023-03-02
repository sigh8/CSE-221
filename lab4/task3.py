inp = open("input3.txt", mode='r')
data = inp.readlines()
lst = list(map(int, data[1].split()))


def merge(lft, right):
    lst = []
    i = j = inversions = 0
    while i < len(lft) and j < len(right):
        if lft[i] <= right[j]:
            lst.append(lft[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
            inversions += len(lft) - i
    lst += lft[i:]
    lst += right[j:]
    return lst, inversions


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    lft, invL = mergeSort(arr[:mid])
    right, invR = mergeSort(arr[mid:])
    merged, invM = merge(lft, right)
    return merged, invL + invR + invM


print(mergeSort(lst)[1])
inp.close()