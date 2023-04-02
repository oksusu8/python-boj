
a, b = map(str, input().split()) # 문자열 타입으로

a = a[::-1]
b = b[::-1]

if a>b:
    print(a)
else:
    print(b)