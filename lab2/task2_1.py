inp = open("input2_4.txt", mode='r')
out = open("output2_4.txt", mode='w')
data = inp.readlines()
lst = []
lst1 = list(map(int, data[1].split()))
lst2 = list(map(int, data[3].split()))
lst = lst1 + lst2
lst.sort()
for i in lst:
    print(i, end=" ", file=out)
inp.close()
out.close()