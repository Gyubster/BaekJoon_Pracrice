String_Input = input()
List = [-1]*26

for i in range(len(String_Input)):
    if List[ord(String_Input[i])-97] != -1:
        continue
    else:
        List[ord(String_Input[i])-97] = i

for i in range(26):
    print(List[i], end=' ')
