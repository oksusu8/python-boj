# 테스트 케이스 개수 t
# 두 정수 a, b

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print('Case #{0}: {1}'.format(i, a+b))
    
#i = 1
#while (i<=t):
#    a, b = map(int, input().split())
#    print('Case #',i,':', a+b)
#    i+=1