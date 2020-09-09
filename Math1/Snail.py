# ClimbUp, ClimbDown, Height = map(int, input().split())
#
# Day = 1
# TotalHeight = 0
#
# while True:
#     if TotalHeight < Height:
#         TotalHeight += ClimbUp
#         if TotalHeight == Height:
#             print(Day)
#         else:
#             TotalHeight -= ClimbDown
#     Day += 1
#
# print(Day)

# 시간 초과로 인해서 다시 작성

ClimbUp, ClimbDown, Height = map(int, input().split())

Day = (Height-ClimbDown)/(ClimbUp-ClimbDown)

print(int(Day) if Day == int(Day) else int(Day)+1)
