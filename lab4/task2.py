inp = open("input2.txt", mode='r')
data = inp.readlines()
lst = list(map(int, data[1].split()))


def find_max(arr, idx, size):
    if size - 1 == 0:
        return arr[idx]
    if idx >= size - 2:
        if arr[idx] > arr[idx + 1]:
            return arr[idx]
        else:
            return arr[idx + 1]
    large = find_max(arr, idx + 1, size)
    if arr[idx] > large:
        return arr[idx]
    else:
        return large


print(find_max(lst, 0, len(lst)))
inp.close()