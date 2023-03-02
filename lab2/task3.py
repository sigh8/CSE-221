inp = open("input3_1.txt", mode='r')
out = open("output3_1.txt", mode='w')
data = inp.readlines()
lst = list(map(int, data[1].split()))
def merge(a, b):
    lst = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            lst.append(a[i])
            i += 1
        else:
            lst.append(b[j])
            j += 1
    lst += a[i:]
    lst += b[j:]
    return lst

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)          # complete the merge function above
arr = mergeSort(lst)
for i in arr:
    print(i, end=" ", file=out)
inp.close()
out.close()