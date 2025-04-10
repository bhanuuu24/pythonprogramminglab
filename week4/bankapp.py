balance = 0
transactions = []

def credit(amount):
    global balance
    balance += amount
    transactions.append(amount)
    print(" credited successfully.\n")

def debit(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!\n")
    else:
        balance -= amount
        transactions.append(amount)
        print(" debited successfully.\n")

def show_balance():
    print(balance)

def last_transactions():
    print("Last 5 transactions:")
    for t in transactions[-5:]:
        print(t)
    print()


while True:
    print("------ Bank Menu ------")
    print("1. Credit amount")
    print("2. Debit amount")
    print("3. Show balance")
    print("4. Last 5 transactions")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        credit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        debit(amount)
    elif choice == '3':
        show_balance()
    elif choice == '4':
        last_transactions()
    elif choice == '5':
        print("Thank you for using the bank application!")
        break
    else:
        print("Invalid choice. Please try again.\n")