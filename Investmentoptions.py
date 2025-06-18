balance = 500.0

def show_investment_options():
    print("\nInvestment Options:")
    print("1. Fixed Deposit - Minimum $100")
    print("2. Stock Market Fund - Minimum $200")
    print("3. Crypto Basket - Minimum $50")
    print("4. Exit")

while True:
    show_investment_options()
    choice = input("Choose an investment option (1-4): ")

    if choice == "1":
        if balance >= 100:
            balance -= 100
            print("✅ You invested in Fixed Deposit. $100 deducted.")
        else:
            print("❌ Not enough balance for Fixed Deposit.")

    elif choice == "2":
        if balance >= 200:
            balance -= 200
            print("✅ You invested in Stock Market Fund. $200 deducted.")
        else:
            print("❌ Not enough balance for Stock Market Fund.")

    elif choice == "3":
        if balance >= 50:
            balance -= 50
            print("✅ You invested in Crypto Basket. $50 deducted.")
        else:
            print("❌ Not enough balance for Crypto Basket.")

    elif choice == "4":
        print("👋 Exiting investment system.")
        break

    else:
        print("⚠️ Invalid option. Please choose 1-4.")

    print(f"💰 Current Balance: ${balance:.2f}")