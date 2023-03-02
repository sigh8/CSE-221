# low  –> Starting index,  high  –> Ending index */
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)  # Before pi
        quickSort(arr, pi + 1, high)  # After pi
    # This function takes last element as pivot, places the pivot element at its correct position in sorted array,
    # and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot


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


array = [10, 7, 8, 9, 1, 5]
quickSort(array, 0, len(array) - 1)

print(f'Sorted array: {array}')
