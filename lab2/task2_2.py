inp = open("input2_4.txt", mode='r')
out = open("output2_4.txt", mode='w')
data = inp.readlines()
lst = []
lst1 = list(map(int, data[1].split()))
lst2 = list(map(int, data[3].split()))
i = j = 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] <= lst2[j]:
        lst.append(lst1[i])
        i += 1
    else:
        lst.append(lst2[j])
        j += 1
lst += lst1[i:]
lst += lst2[j:]
for i in lst:
    print(i, end=" ", file=out)
inp.close()
out.close()