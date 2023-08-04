
from expenses.category import Category
from expenses.budget import Budget
from expenses.espense import Expense


class UI:
    def __init__(self):
        self.budget = Budget(total_budget=1000)  # Задайте начальный бюджет

    def show_menu(self):
        print("1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Отслеживание бюджета")
        print("0. Выход")

    def add_expense(self):
        amount = float(input("Введите сумму расхода: "))
        date = input("Введите дату расхода (ГГГГ-ММ-ДД): ")
        category_name = input("Введите категорию расхода: ")
        description = input("Введите описание расхода: ")

        category = self.budget.get_category(category_name)
        if category is None:
            print("Категория не найдена. Создайте категорию.")
            return

        expense = Expense(amount, date, category, description)
        category.add_expense(expense)
        print("Расход успешно добавлен.")

    def view_expenses(self):
        category_name = input("Введите название категории (или оставьте пустым для просмотра всех расходов): ")
        category = self.budget.get_category(category_name)

        if category:
            expenses = category.get_expenses()
        else:
            expenses = [expense for cat in self.budget.categories.values() for expense in cat.get_expenses()]

        for expense in expenses:
            print(expense)

    def budget_tracking(self):
        print(f"Общий бюджет: {self.budget.get_total_budget()}")
        print(f"Остаток бюджета: {self.budget.get_remaining_budget()}")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.budget_tracking()
            elif choice == "0":
                print("Выход из приложения.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
