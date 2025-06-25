# Dictionary to store user data
users = {
    "user1": {"password": "pass123", "balance": 100},
    "user2": {"password": "abc123", "balance": 200}
}

# Login
print("Welcome to Secure Smart ATM")
username = input("Enter username: ")

if username in users:
    password = input("Enter password: ")
    if password == users[username]["password"]:
        print("Login successful!")
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
                print("Thank you for using Smart ATM. Keep saving!")
                break
            else:
                print("Invalid option. Try again.")

        users[username]["balance"] = balance  # Update balance in dictionary

    else:
        print("Password incorrect.")
else:
    print("User does not exist.")