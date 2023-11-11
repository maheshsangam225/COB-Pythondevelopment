import json
import os
from datetime import datetime

# Initialize an empty list to store expenses
expenses = []

# Create a data file to store expenses
data_file = "expenses.json"

# Load existing expenses from the data file, if it exists
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        expenses = json.load(file)

# Function to add an expense
def add_expense():
    name = input("Enter the name of the expense: ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    category = input("Enter the category of the expense: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"date": date, "name": name, "amount": amount, "category": category})

    with open(data_file, "w") as file:
        json.dump(expenses, file)

    print("Expense added successfully.")

# Function to generate an expense report
def generate_report():
    if not expenses:
        print("No expenses to generate a report.")
        return

    total_expenses = sum(expense["amount"] for expense in expenses)
    print("\nExpense Report:")
    print("-" * 50)
    for expense in expenses:
        print(f"Date: {expense['date']}")
        print(f"Name: {expense['name']}")
        print(f"Category: {expense['category']}")
        print(f"Amount: Rs.{expense['amount']:.2f}")
        print("-" * 50)
    print(f"Total Expenses: Rs.{total_expenses:.2f}")

# Function to edit an expense
def edit_expense():
    if not expenses:
        print("No expenses to edit.")
        return

    print("Select an expense to edit:")
    for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense['name']} ({expense['category']}) - Rs.{expense['amount']:.2f}")

    try:
        choice = int(input("Enter the number of the expense to edit (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(expenses):
            expense = expenses[choice - 1]
            print("Editing Expense:")
            print(f"Name: {expense['name']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: Rs.{expense['amount']:.2f}")
            new_name = input("Enter a new name (leave empty to keep the same): ")
            new_category = input("Enter a new category (leave empty to keep the same): ")
            new_amount = input("Enter a new amount (leave empty to keep the same): ")

            if new_name:
                expense['name'] = new_name
            if new_category:
                expense['category'] = new_category
            if new_amount:
                try:
                    expense['amount'] = float(new_amount)
                except ValueError:
                    print("Invalid amount. Expense not updated.")
                    return

            with open(data_file, "w") as file:
                json.dump(expenses, file)

            print("Expense updated successfully.")
        else:
            print("Invalid choice. Please select a valid expense to edit.")
    except ValueError:
        print("Invalid choice. Please enter a number.")

# Function to delete an expense
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    print("Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense['name']} ({expense['category']}) - Rs.{expense['amount']:.2f}")

    try:
        choice = int(input("Enter the number of the expense to delete (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(expenses):
            deleted_expense = expenses.pop(choice - 1)
            with open(data_file, "w") as file:
                json.dump(expenses, file)
            print(f"{deleted_expense['name']} ({deleted_expense['category']}) - Rs.{deleted_expense['amount']:.2f} deleted.")
        else:
            print("Invalid choice. Please select a valid expense to delete.")
    except ValueError:
        print("Invalid choice. Please enter a number.")

# Function to show a menu of options
def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Edit Expense")
    print("3. Delete Expense")
    print("4. Generate Expense Report")
    print("5. Exit")

# Main program
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        edit_expense()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
