while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = input("Enter amount: ")

        with open("expenses.txt", "a") as f: #this line creaytes a file if it doesn't exist and opens it in append mode
            f.write(name + "," + amount + "\n")#this line writes the name and amount to the file, separated by a comma, and adds a new line at the end

        print("Expense added!")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as f:#this line opens the file in read mode
                data = f.readlines()
                for line in data:
                    name, amount = line.strip().split(",")#this line splits the line into name and amount using comma as a separator
                    print(name, "-", amount)
        except FileNotFoundError:
            print("No expenses found")

    elif choice == "3":
        total = 0
        try:
            with open("expenses.txt", "r") as f:#this line opens the file in read mode
                for line in f:
                    name, amount = line.strip().split(",")
                    total += float(amount)
            print("Total Amount:", total)
        except FileNotFoundError:
            print("No data available")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")