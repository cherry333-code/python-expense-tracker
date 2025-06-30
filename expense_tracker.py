import json
import os
from datetime import datetime

expenses = []

# Load existing expenses from file
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            return json.load(f)
    return []

# Save expenses to file
def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

# Add new expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹ "))
        category = input("Enter category (Food, Travel, etc.): ").capitalize()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print("✅ Expense added!\n")
    except ValueError:
        print("❌ Invalid input. Try again.\n")

# Show summary
def view_summary():
    total = sum(e['amount'] for e in expenses)
    print(f"\n📊 Total Expenses: ₹ {total:.2f}")

    by_category = {}
    for e in expenses:
        cat = e['category']
        by_category[cat] = by_category.get(cat, 0) + e['amount']

    print("Expenses by Category:")
    for cat, amt in by_category.items():
        print(f" - {cat}: ₹ {amt:.2f}")
    print()

# Main menu loop
def menu():
    global expenses
    expenses = load_expenses()

    while True:
        print("========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_expenses()
            print("💾 Data saved. Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.\n")

# Run the app
if __name__ == "__main__":
    menu()
