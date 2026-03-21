while True:
    print("Welcome to the login system!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("user.txt", "a") as f:
            f.write(username + ","+ password + "\n")
        print("Registration successful!")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open("user.txt","r") as f:
                data = f.readlines()
                for line in data:
                    stored_username , stored_password = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        print("Login successful!")
                        break
                else:                    print("Invalid username or password")
        except FileNotFoundError:
            print("No users found. Please register first.")     
    elif choice == "3":
        print("Exiting...")
        break   
