n = input("Enter a string: ")
freq ={}
for char in n:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
for i in range(len(n)):
    if freq[n[i]] == 1:
        print("First unique character is:", n[i])
        break
