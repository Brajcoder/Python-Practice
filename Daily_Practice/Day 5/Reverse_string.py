S = input("Enter the string to reverse: ")
left = 0
right = len(S) - 1
s = list(S)
while left < right:
    (s[left], s[right]) = (s[right], s[left])
    left += 1
    right -= 1  
print("Reversed string is: ", ''.join(s))