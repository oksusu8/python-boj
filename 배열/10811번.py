# 바구니 개수 : n / 역순 만드는 횟수 : m
n, m = map(int, input().split())

# 바구니 번호 1 ~ n번 부여
basket = [i for i in range(1,n+1)] 
print(basket)  # [1,2,3,4,5]

a=[]
i, j = map(int, input().split())
for k in range(i-1, j):
    a.reverse(basket[k])
print(a)



'''
a=[]
for i in range(n):
    a.append(basket[n-1-i])
    
for _ in range(m):
    i, j = map(int, input().split())
    '''



'''

print(basket[5-1-0])
a = []
a[0] = basket[4]
a[1] = basket[3]
a[2] = basket[2]
a[3] = basket[1]
a[4] = basket[0]'''