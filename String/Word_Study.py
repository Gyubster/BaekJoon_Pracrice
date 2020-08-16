Str_Input = input().upper()
List = []

for i in set(Str_Input):
    List.append(Str_Input.count(i))
Max_Count = [i for i, x in enumerate(List) if x == max(List)]

# 해야됨
