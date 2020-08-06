Number_List = []

for i in range(9):
    a = int(input())
    Number_List.append(a)

print(max(Number_List))

for i in range(9):
    if Number_List[i] == max(Number_List):
        print (i+1)

#  왜 Number_List.append(int(input())) 는 안되는지..?