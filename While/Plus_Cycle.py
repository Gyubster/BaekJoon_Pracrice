import sys

Number1 = int(sys.stdin.readline())
Number1_Second_Digit = Number1 // 10
Number1_First_Digit = Number1 % 10

n = 0

while True:
    Number = Number1_Second_Digit + Number1_First_Digit
    Number_First_Digit = Number % 10
    Number = Number1_First_Digit*10 + Number_First_Digit
    if Number1 != Number:
        n = n +1
    else:
        print(n)