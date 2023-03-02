inp = open("input3.txt", mode='r')
data = inp.readlines()
q = []


def heapify(q, i):
    while i > 0:
        parent = (i - 1) // 2
        if q[i][1] < q[parent][1]:
            q[i], q[parent] = q[parent], q[i]
            i = parent
        else:
            break


def sink(q, i):
    l = 2 * i + 1
    r = 2 * i + 2
    small = i
    if l < len(q) and q[l][1] < q[small][1]:
        small = l
    if r < len(q) and q[r][1] < q[small][1]:
        small = r
    if small != i:
        q[i], q[small] = q[small], q[i]
        sink(q, small)


def enque(name, level, q):
    q.append((name, level))
    heapify(q, len(q)-1)


def seeDoctor(q):
    if not q:
        print("No patients in queue.")
        return
    q[0], q[-1] = q[-1], q[0]
    name, level = q.pop()
    sink(q, 0)
    return name


def printQueue(q):
    if not q:
        print("No patients in queue.")
        return
    for i in q:
        print(i[0])


def appointment(data, q):
    for i in data:
        name, level = i.split()
        if name == 'see':
            print(seeDoctor(q))
        else:
            enque(name, int(level), q)


appointment(data, q)
inp.close()