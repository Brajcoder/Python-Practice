password = input("Enter your password: ")
upper = 0
lower = 0
number = 0  
symbol = 0
for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        number += 1
    else:
        symbol += 1
if len(password)<6:
    print("Password is too short. It should be at least 6 characters long.")
elif len(password)>=8 and upper and lower and number and symbol:
    print("Password is strong.")
else:
    print("Medium strength password.")