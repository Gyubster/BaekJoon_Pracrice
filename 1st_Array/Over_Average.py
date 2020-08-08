Input_Number = int(input())

for i in range(Input_Number):
    Sum = 0
    n = 0
    Num_List = list(map(int, input().split()))

    for j in range(1, len(Num_List)):
        Sum += Num_List[j]

    Avg = Sum/(len(Num_List)-1)

    for k in range(1,len(Num_List)):
        if Num_List[k] > Avg:
            n+=1

    Total_Percent = float(n/(len(Num_List)-1)*100)
    Round_Total_Percent = round(Total_Percent, 3)

    print('%0.3f' %Round_Total_Percent + '%')

