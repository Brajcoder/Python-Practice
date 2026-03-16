n =  int(input())
ar = list(map(int,input().split()))
result = 0
for i in range(n):
    result+=ar[i]
    
print(result)