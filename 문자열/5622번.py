word = input()
num_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0

for i in range(len(word)):
    for j in num_list:
        if word[i] in j:
            time +=num_list.index(j)+3
            
print(time)
            