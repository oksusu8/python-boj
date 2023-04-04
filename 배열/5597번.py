
student = []
absent=[]

for i in range(28):
    n = int(input())
    student.append(n)
    
for k in range(1, 31):
    if k not in student:
        absent.append(k)
    
print(absent[0])
print(absent[1])


# 효율적인 코드가 있지 않을까...?