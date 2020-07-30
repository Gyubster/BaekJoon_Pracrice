a = input()
b = input()

a = int(a)
b = int(b)

hundred = b//100
ten = (b%100)//10
one = b%10

line_1 = a * one
line_2 = a * ten
line_3 = a * hundred
line_4 = a * b

print(line_1)
print(line_2)
print(line_3)
print(line_4)