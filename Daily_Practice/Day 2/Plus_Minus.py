n = int(input())
arr = list(map(int, input().split()))

positive = 0
negative = 0    
zero = 0
for i in range(n):
    if arr[i] > 0:
        positive += 1
    elif arr[i] < 0:
        negative += 1
    else:
        zero += 1
print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))  
print("{:.6f}".format(zero/n))