import json
from datetime import datetime

expenses = []

# Load existing data from file
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []

# Save data to file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = datetime.now().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses()
        print("Expense added successfully!\n")

    except:
        print("Invalid input!\n")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['date']}")
    print()

# Calculate total
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: ₹{total}\n")

# Filter by category
def filter_category():
    cat = input("Enter category to filter: ")
    found = False

    for exp in expenses:
        if exp["category"].lower() == cat.lower():
            print(f"₹{exp['amount']} | {exp['date']}")
            found = True

    if not found:
        print("No matching category found.")
    print()

# Menu
def menu():
    load_expenses()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_category()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

# Run program
menu()