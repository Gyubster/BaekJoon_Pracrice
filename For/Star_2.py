Number = int(input())

for i in range(1, Number+1):
    a = '*'*(i)
    print(a.rjust(Number))

# rjust(i): i 만큼 우측으로 정렬
# ljust(i): i 만큼 좌측으로 정렬