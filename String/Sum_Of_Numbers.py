Number_Input1 = int(input())
Number_Input2 = input()

Number_List = list(map(int, Number_Input2))

sum = 0

for i in range(Number_Input1):
    sum += Number_List[i]

print(sum)