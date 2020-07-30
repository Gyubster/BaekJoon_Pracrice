a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

line_1 = (a+b)%c
line_2 = ((a%c)+(b%c))%c
line_3 = (a*b)%c
line_4 = ((a%c)*(b%c))%c

print(line_1)
print(line_2)
print(line_3)
print(line_4)

