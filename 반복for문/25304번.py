# 영수증 총 금액 x
# 구매한 물건 종류의 수 n 
# 각 물건 가격 a, 개수 b
# 계산 후 실제 총 금액 tot

x = int(input())
n = int(input())

tot = 0 # 진짜 합산 가격

for i in range(1, n+1):
    a, b = map(int, input().split()) # 물건의 개수만큼 입력을 받아야하므로, for문 안에
    tot += (a*b) # 입력 받고, 진짜 합산 가격에 저장

if x == tot : 
    print('Yes')
else:
    print('No')