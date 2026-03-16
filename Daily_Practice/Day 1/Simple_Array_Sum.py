# Description

# Given an array of integers, find the sum of all elements in the array.
Array = list(map(int,input().split()))
n = len(Array)
sum = 0
for i in range(n):
    sum+=Array[i]
print(sum)