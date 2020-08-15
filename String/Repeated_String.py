Number_Input = int(input())
Output = ''

for i in range(Number_Input):
    Data_Input = input()
    A_Input, B_Input = Data_Input.split()
    A_Input = int(A_Input)
    for i in range(len(B_Input)):
        Output += B_Input[i]*A_Input
    print(Output)
    Output = ''