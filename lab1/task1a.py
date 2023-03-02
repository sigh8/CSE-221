inp_file = open("/content/drive/MyDrive/cse221/lab1/input1a.txt.txt", mode = "r")
data = inp_file.readlines()
outFile = open("/content/drive/MyDrive/cse221/lab1/output1a.txt.txt", mode = "w")

for i in range(1, int(data[0])+1):
  if int(data[i])%2 == 0:
    print(f"{int(data[i])} this is even", file = outFile)
  else:
    print(f"{int(data[i])} this is odd", file = outFile)
inp_file.close()
outFile.close()