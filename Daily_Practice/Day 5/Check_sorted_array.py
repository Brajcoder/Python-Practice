nums = list(map(int,input("Enter the list of numbers: ").split()))
if nums == sorted(nums):
    print("The array is sorted.")
else:
    print("The array is not sorted.")