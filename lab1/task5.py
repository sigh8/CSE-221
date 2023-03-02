#task5
inp_file = open("/content/drive/MyDrive/cse221/lab1/input5.txt", mode = "r")
data = inp_file.readlines()
outFile = open("/content/drive/MyDrive/cse221/lab1/output5.txt", mode = "w")
train = []
for i in range(1, int(data[0])+1):
  train.append(data[i][:-1])
train.sort()
for i in range(len(train)-1):
  temp1 = train[i].split()
  temp2 = train[i+1].split()
  if temp1[0] == temp2[0]:
    if temp1[-1] < temp2[-1]:
      tr_tmp = train[i]
      train[i] = train[i+1]
      train[i+1] = tr_tmp
for i in train:
  print(i, file = outFile)
inp_file.close()
outFile.close()