import sys

Number_Input = int(sys.stdin.readline())

for i in range(0, Number_Input):
    a = ' '*i+'*'*(2*(Number_Input-i)-1)
    print(a)

for i in range(1, Number_Input):
    a = ' '*(Number_Input-i-1)+'*'*(2*(i+1)-1)
    print(a)