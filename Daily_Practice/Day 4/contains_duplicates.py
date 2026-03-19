nums = list(map(int, input("Enter numbers separated by space: ").split()))
if len(nums) != len(set(nums)):
    print("True")
else:
    print("False")
    