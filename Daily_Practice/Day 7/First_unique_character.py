s = list(input("Enter a string: "))
freq={}
for char in s:
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1
for i in range(len(s)):
    if freq[s[i]]==1:
        print(i) 
print("NO repeated character")