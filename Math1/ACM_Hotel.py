TestCase = int(input())

for i in range(TestCase):
    H, W, N = map(int, input().split())
    Floor = N%H
    Room = N//H + 1

    if N%H == 0:
        Floor = H
        Room -=1
        
    RoomNumber = Floor*100+Room

    print(RoomNumber)
