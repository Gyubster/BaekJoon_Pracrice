n = 1

try:
    while n > 0:
        A, B = map(int, input().split())
        n = A+B
        print(n)
except:
    exit()

# try, except를 활용하여 오류상황에 따른 exit을 제공한다.
# try 안에서의 상황에서 오류가 나오면 except의 실행문 발동.