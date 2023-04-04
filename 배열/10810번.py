# 바구니 개수 : m, 공 넣기 횟수 : n
m, n = map(int, input().split())

# 처음에는  바구니에 아무것도 없으니, [0,0,0,0,0] 상태
'''
basket = []
for i in range(m):
    basket.append(0)
    이렇게 작성하기 보다는'''
basket= [0]*m #로 작성

'''
i,j,k= map(int, input().split())
basket[i-1] = k
basket[j-1] = k
print(basket)''' #의 원리를 적용했을 때

for _ in range(n):
    i,j,k= map(int, input().split()) # n번 횟수만큼 입력을 받고
    for _ in range(i-1, j): # 해당 범위에 채워 나가는
        basket[i-1] = k
        i=i+1

for a in basket: # 그 후 출력
    print(a, end=' ')

 


