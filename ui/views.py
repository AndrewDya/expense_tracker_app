class MainMenuView:
    @staticmethod
    def show_menu():
        print("1. Добавить расход")
        print("2. Просмотреть расходы")
        print("3. Отслеживание бюджета")
        print("0. Выход")


class ExpenseInputView:
    @staticmethod
    def get_expense_details():
        amount = float(input("Введите сумму расхода: "))
        date = input("Введите дату расхода (ГГГГ-ММ-ДД): ")
        category_name = input("Введите категорию расхода: ")
        description = input("Введите описание расхода: ")
        return amount, date, category_name, description


class ExpenseListView:
    @staticmethod
    def show_expenses(expenses):
        for expense in expenses:
            print(expense)


class BudgetTrackingView:
    @staticmethod
    def show_budget_info(total_budget, remaining_budget):
        print(f"Общий бюджет: {total_budget}")
        print(f"Остаток бюджета: {remaining_budget}")

    @staticmethod
    def category_not_found():
        print("Категория не найдена. Создайте категорию.")
