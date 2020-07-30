Test_Case = int(input())

for i in range(Test_Case):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print('Case #{Number}:'.format(Number=i+1), a+b)

# print에서 다양한 변수를 한번에 출력시 .format을 이용하여 출력
