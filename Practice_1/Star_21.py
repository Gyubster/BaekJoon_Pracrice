import sys

Input_Number = int(sys.stdin.readline())

Even = Input_Number//2
Odd = Input_Number - Input_Number//2

for i in range(Input_Number):
    print('* '*Odd)
    print(' *'*Even)