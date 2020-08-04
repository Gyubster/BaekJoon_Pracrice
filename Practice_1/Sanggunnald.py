import sys

Hamburger = []
for i in range(3):
    Hamburger.append(int(sys.stdin.readline()))

Drink = []
for i in range(2):
    Drink.append(int(sys.stdin.readline()))

Set_List = []
for i in range(3):
    for j in range(2):
        Set_List.append(Hamburger[i] + Drink[j] - 50)

print(min(Set_List))