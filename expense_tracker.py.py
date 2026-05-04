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

# Save expenses to file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file,indent=4)

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: ").strip())
        if amount<=0:
            print('Amount must be greater than 0!\n')
            return
        category = input("Enter category: ").strip()
        if not category:
            print('Category cannot be empty!\n')
            return
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
        print("Invalid input! Please enter correct values.\n")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    print('\n===== All Expenses =====')
    for i, exp in enumerate(expenses, 1):
        print(f"{i}.Amount: ₹{exp['amount']} | Category: {exp['category']} | Date: {exp['date']}")
    print()

# Calculate total
def total_expense():
    if not expenses:
        print('No Expenses to calculate.\n')
        return
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: ₹{total}\n")

# Filter by category
def filter_category():
    cat = input("Enter category to filter: ").strip()
    found = False
    print('\n===== Filtered Expenses =====')
    for exp in expenses:
        if exp["category"].lower() == cat.lower():
            print(f"Amount: ₹{exp['amount']} | Date: {exp['date']}")
            found = True

    if not found:
        print("No matching category found.")
    print()

# Delete expense
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: ").strip()) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses()
            print(f"🗑️ Deleted: ₹{removed['amount']} ({removed['category']})\n")
        else:
            print("❌ Invalid index!\n")

    except:
        print("❌ Invalid input!\n")

def search_by_date():
    date_input = input("Enter date (YYYY-MM-DD): ").strip()
    found = False

    print("\n===== Expenses on Given Date =====")
    for exp in expenses:
        if exp["date"] == date_input:
            print(f"Amount: ₹{exp['amount']} | Category: {exp['category']}")
            found = True

    if not found:
        print("No expenses found for this date.")
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
        print("5. Delete Expense")
        print("6. Search by Date")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            search_by_date()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
    break

# Run program
menu()
