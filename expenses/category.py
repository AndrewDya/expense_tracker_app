class Category:
    def __init__(self, name, budget_limit):
        self.name = name
        self.budget_limit = budget_limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def get_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def __str__(self):
        return f"Category: {self.name}, Budget Limit: {self.budget_limit}"
