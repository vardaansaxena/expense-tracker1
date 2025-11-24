Expense Tracker - Explanation

1. display_menu()
   - This function shows the list of options for the user.
   - Options are: Add Expense, List Expenses, Save, Load, Exit.

2. add_expense(expenses)
   - Asks the user to enter:
       amount of expense
       category (like food, travel)
       date
       description
   - It makes a dictionary for the expense.
   - Then it adds that dictionary to the expenses list.

3. list_expenses(expenses)
   - If there are no expenses, it prints "No expenses recorded."
   - Otherwise, it prints every expense with:
       amount, category, date, description.

4. save_expenses(expenses, filename="expenses.txt")
   - Opens the file "expenses.txt" in write mode.
   - Saves each expense in one line using commas.
   - Example line saved:
       200,Food,2024-10-10,Lunch
   - Shows a message when saving is done.

5. load_expenses(filename="expenses.txt")
   - Reads the file line by line.
   - Breaks each line into 4 parts using commas.
   - Converts amount into a number.
   - Makes a dictionary for each expense and adds to the list.
   - Shows how many expenses were loaded.

6. main()
   - Keeps running in a loop.
   - Shows the menu and asks the user to choose an option.
   - Based on user choice:
       1 → add expense
       2 → list expenses
       3 → save expenses to file
       4 → load expenses from file
       5 → exit the program

7. Program ends when user chooses option 5.
