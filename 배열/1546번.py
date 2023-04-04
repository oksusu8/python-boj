
n = int(input()) # 과목 개수
score = list(map(int, input().split()))
sum = 0 # 조작 이후 모든 과목 점수 합

for i in score:
    i = i/max(score)*100
    sum += i
    
print(sum/n)
    