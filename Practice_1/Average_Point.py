import sys

Score = []
Total_Score = 0

for i in range(5):
    Individual_Score = int(sys.stdin.readline())
    Score.append(Individual_Score)
    if Score[i] < 40:
        Score[i] = 40

for i in range(5):
    Total_Score += Score[i]

Answer = int(Total_Score/5)
print(Answer)

# List에 각 요소에 대한 값이 지정이 안되있으면, append 혹은 insert로 값을 넣어주는 식으로 생각.
