def display_menu():
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Save Expenses")
    print("4. Load Expenses")
    print("5. Exit")

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter numeric value.")
        return
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nExpenses:")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Description: {expense['description']}")
    print()

def save_expenses(expenses, filename="expenses.txt"):
    try:
        with open(filename, "w") as f:
            for expense in expenses:
                # Save as comma separated values
                line = f"{expense['amount']},{expense['category']},{expense['date']},{expense['description']}\n"
                f.write(line)
        print(f"Expenses saved to {filename}")
    except Exception as e:
        print(f"Error saving expenses: {e}")

def load_expenses(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",", 3)
                    if len(parts) == 4:
                        try:
                            amount = float(parts[0])
                        except ValueError:
                            print(f"Skipping invalid amount in line: {line}")
                            continue
                        category = parts[1]
                        date = parts[2]
                        description = parts[3]
                        expense = {
                            "amount": amount,
                            "category": category,
                            "date": date,
                            "description": description
                        }
                        expenses.append(expense)
                    else:
                        print(f"Skipping invalid line: {line}")
        print(f"Loaded {len(expenses)} expenses from {filename}")
    except FileNotFoundError:
        print(f"No saved expenses found in {filename}")
    except Exception as e:
        print(f"Error loading expenses: {e}")
    return expenses

def main():
    expenses = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
        elif choice == "4":
            expenses = load_expenses()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
