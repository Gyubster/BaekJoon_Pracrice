
FundamentalCost, ManufactureCost, ProductPrice  = map(int, input().split())
n = 1

while True:
    if FundamentalCost + ManufactureCost*n >= ProductPrice*n:
        n+=1

    else:
        break

print(n)
