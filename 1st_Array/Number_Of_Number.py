a = int(input())
b = int(input())
c = int(input())

Number_Str = str(a*b*c)
Number_List = []
Len_Number = len(Number_Str)

for i in range(Len_Number):
    Number_List.append(int(Number_Str[i]))

for i in range(10):
    print(Number_List.count(i))

# arr = [int(i) for i in str(a*b*c)]
