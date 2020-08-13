a = int(input())
n = 0

for i in range(1, a+1):
    if i < 100:
        n += 1
    else:
        Number_List = list(map(int, str(i)))
        if Number_List[0] - Number_List[1] == Number_List[1] - Number_List[2]:
            n += 1

print(n)