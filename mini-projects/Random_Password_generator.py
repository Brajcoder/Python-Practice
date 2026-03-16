import random # Import the random module to generate random characters
aplhabet = "abcdefghijklmnopqrstuvwxyz"
Numbers = "0123456789"  
Symbols = "!@#$%^&*()_+"
characters = aplhabet + Numbers + Symbols  # Combine all character sets into one string

password = ""
n = int(input("Enter the length of the password: "))
for i in range(n):
    password += random.choice(characters) # Randomly select a character from the combined string and add it to the password

print("Generated Password: ", password)