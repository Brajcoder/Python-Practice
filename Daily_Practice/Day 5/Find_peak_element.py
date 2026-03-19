nums = list(map(int,input("Enter the list of numbers: ").split()))
n = len(nums)
for i in range(1,n):
    if (i==0 or nums[i-1] < nums[i]) and(i==n-1 or nums[i]  > nums[i+1]):
        Print("Element found ",nums[i])
    else:
        print("NO Element found")