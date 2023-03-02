inp = open("input3.txt", mode='r')
data = inp.readlines()
q = []


def enque(name, level, q):
    q.append((name, level))
    for i in range(len(q)):
        for j in range(0, len(q)-i-1):
            if q[j][1] > q[j+1][1]:
                q[j], q[j+1] = q[j+1], q[j]


def seeDoctor(q):
    if not q:
        print("No patients in queue.")
        return
    name, level = q.pop(0)
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