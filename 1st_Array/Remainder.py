Numbers_List = []
New_Numbers_List = []

for i in range(10):
    a = int(input())%42
    Numbers_List.append(a)

for v in Numbers_List:
    if v not in New_Numbers_List:
        New_Numbers_List.append(v)

print(len(New_Numbers_List))

