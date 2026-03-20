nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
common = []
if len(nums1)>len(nums2):
    for num in set(nums1):
        if num in nums2:
            common.append(num) 
else:
    for num in set(nums2):
        if num in nums1:
            common.append(num)
print(common)