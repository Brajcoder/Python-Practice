nums = list(map(int,input("Enter the list of numbers: ").split()))
nums = sorted(nums)
for i in range(len(nums)+1):
    if i not in nums:
        print(i)