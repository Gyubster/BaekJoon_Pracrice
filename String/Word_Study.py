Str_Input = input().upper()
List = []

for i in set(Str_Input):
    List.append(Str_Input.count(i))

Max_Count = [i for i, x in enumerate(List) if x == max(List)]

if len(Max_Count)>1:
    print("?")
else:
    print(list(set(Str_Input))[List.index(max(List))])

# emurate를 이용하여 최대값이 있는 위치를 알게함.
