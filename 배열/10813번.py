# 바구니 개수 : n / 공 교환 횟수 : m
n, m = map(int, input().split())

# n = 5개(0,1,2,3,4) m=4번
basket = [i+1 for i in range(n)] # n만큼 돌아가는데 인덱스라 1 더해줌

'''
i = 1; j = 2
a = basket[i-1]
print(a)
basket[i-1] = basket[j-1]
basket[j-1] = a
print(basket)'''


for _ in range(m):
    i, j = map(int, input().split())
    a = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = a


for k in basket:
    print(k, end=' ')
