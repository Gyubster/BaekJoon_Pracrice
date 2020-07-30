Test_Case = int(input())

for i in range(Test_Case):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print('Case #{Number}:'.format(Number=i+1),a,'+',b, '=', a+b)