import sys

a, b, c = sys.stdin.readline().split()
a = int(a)
b = int(b)
c = int(c)

Num_List = []
Num_List.append(a)
Num_List.append(b)
Num_List.append(c)

Num_List.sort()
print(Num_List[1])
