Number_List = list(range(1,10000))
Generated_Number_List = []

for i in range(1, 10000):
    a = i
    b = i + sum(int(j) for j in str(a))
    Generated_Number_List.append(b)

Result_List = list(set(Number_List) - set(Generated_Number_List))
Result_List.sort()

for j in range(len(Result_List)):
    print(Result_List[j])