ClimbUp, ClimbDown, Height = map(int, input().split())

Day = (Height-ClimbDown)/(ClimbUp-ClimbDown)

print(int(Day) if Day == int(Day) else int(Day)+1)
