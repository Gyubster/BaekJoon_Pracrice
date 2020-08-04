import sys

Number_Input = int(sys.stdin.readline())

for i in range(1, Number_Input+1):
    print('*'*i)

for i in reversed(range(1, Number_Input)):
    print('*'*i)