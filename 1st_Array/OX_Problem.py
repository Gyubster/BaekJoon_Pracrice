Test_Case = int(input())

for i in range(Test_Case):
    Case = input()
    Score = 0
    n = 0
    for j in range(len(Case)):
        if Case[j] == 'O':
            n += 1
            Score += n

        elif Case[j] == 'X':
            n = 0
            Score += 0

    print(Score)
