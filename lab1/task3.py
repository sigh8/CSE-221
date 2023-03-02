#task3
inp_file = open("/content/drive/MyDrive/cse221/lab1/input3.txt", mode = "r")
data = inp_file.readlines()
outFile = open("/content/drive/MyDrive/cse221/lab1/output3.txt", mode = "w")
arr = list(map(int, data[1].split()))
def bubbleSort(arr):
  for i in range(len(arr)-1):
    swap = False
    for j in range(len(arr)-i-1):
      # in best case scenerio the code will not enter this condition and so "swap" will remain False
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap = True
    if swap is False:  #as "swap" is still False it will break out of the loop
      break
bubbleSort(arr)
for i in arr:
  print(i, file = outFile)
inp_file.close()
outFile.close()