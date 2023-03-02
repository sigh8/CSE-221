inp = open("/content/drive/MyDrive/cse221/lab1/input1b.txt.txt", mode = "r")
data = inp.readlines()
out = open("/content/drive/MyDrive/cse221/lab1/output1b.txt.txt", mode = "w")

for i in range(1,int(data[0])+1):
  temp = data[i][10:].split()
  if temp[1] == '+':
    print(f"The result of {temp[0]} {temp[1]} {temp[2]} is {int(temp[0])+int(temp[2])}", file = out)
  if temp[1] == '-':
    print(f"The result of {temp[0]} {temp[1]} {temp[2]} is {int(temp[0])-int(temp[2])}", file = out)
  if temp[1] == '/':
    print(f"The result of {temp[0]} {temp[1]} {temp[2]} is {int(temp[0])/int(temp[2])}", file = out)
  if temp[1] == '*':
    print(f"The result of {temp[0]} {temp[1]} {temp[2]} is {int(temp[0])*int(temp[2])}", file = out)
inp.close()
out.close()