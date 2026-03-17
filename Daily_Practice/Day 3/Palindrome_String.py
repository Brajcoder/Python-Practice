n = input("Enter a string: ")
string = ""
for char in n:
    if char.isalnum():
        string += char.lower()
print(string == string[::-1])