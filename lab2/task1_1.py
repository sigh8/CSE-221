inp = open("input1_4.txt", mode='r')
out = open("output1_4.txt", mode='w')
data = inp.readlines()
info = list(map(int, data[0].split()))
lst = list(map(int, data[1].split()))
for i in range(info[0]):
    sub = info[1] - lst[i]
    if i != len(lst)-1:
        for j in range(i+1, len(lst)):
            if lst[j] == sub:
                print(f"{i+1} {j+1}", file=out)
                quit()
print("IMPOSSIBLE", file=out)
inp.close()
out.close()
