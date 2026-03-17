n = input("Enter a string: ")
n = n.lower()
frequency = {}
for char in n:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)