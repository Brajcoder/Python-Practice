n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
primary_diagonal = 0
secondary_diagonal = 0
for i in range(n):
    primary_diagonal += arr[i][i]
    secondary_diagonal += arr[i][n - 1 - i]
print(abs(primary_diagonal - secondary_diagonal))