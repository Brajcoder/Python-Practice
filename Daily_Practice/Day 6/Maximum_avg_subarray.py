nums = list(map(int, input().split()))
k = int(input())
max_sum = sum(nums[:k])   # here we are calculating the sum of the first 'k' elements to initialize max_sum
current_sum = max_sum # we will use current_sum to keep track of the sum of the current window of size 'k'
for i in range(k, len(nums)):
    current_sum += nums[i] - nums[i - k] # we add the next element in the array and remove the first element of the previous window to maintain the size of 'k'
    max_sum = max(max_sum, current_sum) # we update max_sum if the current_sum is greater than the max_sum
print(max_sum / k)