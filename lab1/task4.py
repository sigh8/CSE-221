#task4
inp_file = open("/content/drive/MyDrive/cse221/lab1/input4.txt", mode = "r")
data = inp_file.readlines()
outFile = open("/content/drive/MyDrive/cse221/lab1/output4.txt", mode = "w")
id = data[1].split()
marks = data[2].split()
for i in range(int(data[0])):
  high = i
  for j in range(i+1,len(marks)):
    if marks[high] < marks[j]:
      high = j
    elif marks[high] == marks[j]:
      if id[j] < id[i]:
        high = j
  marks[i],marks[high] = marks[high],marks[i]
  id[i],id[high]=id[high],id[i]
  print('ID:',id[i],'Mark:',marks[i], file = outFile)
inp_file.close()
outFile.close()