"""Initialize a class called ExpenseTracker:


Function add_expense: 
    Adds expenses as objects to the list using description, amount and category

Function view_expenses():
    If the list of expenses is empty, displays that no expenses are recorded
    else:
    Shows all expenses that are in the list

Function filter_expenses_by_category():
Filters expenses based on category, if it exists, it will display expenses
according to category


Function generate_summary_report():
Prints out summary based on description,amount,category and expense

Function menu():
    Repeat until user chooses to exit:
        Print menu options:
            "1. Add expense"
            "2. View expenses"
            "3. Filter expenses by category"
            "4. Generate summary report"
            "5. Exit"
        Ask user to choose an option
        

        If user chooses '1':
            Ask for description, amount, and category
            Call add_expense(description, amount, category)
        If user chooses '2':
            Call view_expenses()
        If user chooses '3':
            Ask for category to filter
            Call filter_expenses_by_category(category)
        If user chooses '4':
            Call generate_summary_report()
        If user chooses '5':
            Print "Exiting the program."
            Exit the loop and end the program
"""


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = {
            'description': description,
            'amount': amount,
            'category': category
        }
        self.expenses.append(expense)
        print("Expense added.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for i in self.expenses:
                print(f"Description: {i['description']}, Amount: ${i['amount']}, Category: {i['category']}")

    def filter_expenses_by_category(self, category):
        is_found = False

        for i in self.expenses:
            if i['category'] == category:
                is_found = True


        if is_found == False:
            print(f"No expenses found in category: {category}")
        else:
            for i in self.expenses:
                if i['category'] == category:
                    print(f'Description: {i['description']}, amount: {i['amount']}, category: {i['category']}')
    def generate_summary_report(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            summary = {}
            for expense in self.expenses:
                if expense['category'] not in summary.keys():
                    summary[expense['category']] = expense['amount']
                else:
                    summary[expense['category']] += expense['amount']

            print("Summary Report:")
            for category, total_amount in summary.items():
                print(f"{category}: {total_amount}")

    def menu(self):
        while True:
            print("1. Add expense")
            print("2. View expenses")
            print("3. Filter expenses by category")
            print("4. Generate summary report")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                description = input("Enter description: ")
                amount = int(input("Enter amount: "))
                category = input("Enter category: ")
                self.add_expense(description, amount, category)
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                category = input("Enter category to filter: ")
                self.filter_expenses_by_category(category)
            elif choice == '4':
                self.generate_summary_report()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please choose a valid option.")

expense_tracker = ExpenseTracker()
expense_tracker.menu()