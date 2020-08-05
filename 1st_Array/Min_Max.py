import sys

Input_Number =  int(sys.stdin.readline())
Numbers = list(map(int, sys.stdin.readline().split()))
Numbers.sort()

print(Numbers[0], Numbers[Input_Number-1])
