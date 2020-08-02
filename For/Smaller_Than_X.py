N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

# map(function_to_apply, list_of_inputs)
# iterlator를 list로 표현시키는 방식. 한줄로 표현하기에 매우 유용함. 