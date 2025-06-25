users = {
    "grinch": {"password": "orange", "balance": 500},
    "lynch": {"password": "apple", "balance": 500},
    "ortiz": {"password": "david", "balance": 500}
}

print("Welcome to Capital Digital ATM")

while True:
    print("\nPlease choose an option:")
    print("1. Sign In")
    print("2. Sign Up")
    option = input("Enter 1 or 2: ")

    if option == "1":
        username = input("Enter username: ")
        if username in users:
            while True:
                password = input("Enter password: ")
                if password == users[username]["password"]:
                    print("Login successful!")
                    break
                else:
                    print("Password incorrect. Please try again.")
            break  
        else:
            print("Username not found. Please sign up.")
    
    elif option == "2":
        username = input("Choose a username: ")
        if username in users:
            print("Username already exists. Try signing in or use a different name.")
        else:
            password = input("Create a password: ")
            users[username] = {"password": password, "balance": 0}
            print("Account created successfully! You can now use the ATM.")
            break 
    else:
        print("Invalid option. Please enter 1 or 2.")

balance = users[username]["balance"]

while True:
    print("\nYour current balance is: $" + str(balance))
    print("Choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Invest")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"${amount} deposited successfully!")
        print("Great job growing your savings!")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Not enough funds.")

    elif choice == "3":
        print(f"Your balance is: ${balance}")

    elif choice == "4":
        invest_amount = float(input("Enter amount to invest: "))
        if invest_amount <= balance:
            profit = invest_amount * 0.10
            balance += profit
            print(f"You earned ${profit:.2f} profit from investment!")
            print("Smart investing leads to smart returns!")
        else:
            print("Not enough balance to invest.")

    elif choice == "5":
        print("Thank you for using Capital Digital ATM. Keep saving!")
        break
    else:
        print("Invalid option. Try again.")

users[username]["balance"] = balance