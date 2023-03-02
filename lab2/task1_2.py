inp = open("input1_4.txt", mode='r')
out = open("output1_4.txt", mode='w')
data = inp.readlines()
info = list(map(int, data[0].split()))
lst = list(map(int, data[1].split()))
dic = {}
for i in range(info[0]):
    sub = info[1] - lst[i]
    if sub in dic:
        print(f"{dic[sub]+1} {i+1}", file=out)
        quit()
    dic[lst[i]] = i
print("IMPOSSIBLE", file=out)
inp.close()
out.close()
