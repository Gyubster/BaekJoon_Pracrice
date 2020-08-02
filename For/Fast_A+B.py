import sys

Test_Case = int(input())
for i in range(Test_Case):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(A + B)
