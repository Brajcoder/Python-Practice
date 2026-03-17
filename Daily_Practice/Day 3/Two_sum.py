l = list(map(int,input().split()))
target = int(input())
freq ={}
for i in range(len(l)):
    remain = target - l[i]
    if remain in freq:
        print(freq[remain], i  )
    else:
        freq[l[i]] = i
