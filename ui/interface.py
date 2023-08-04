import tkinter as tk
from tkinter import messagebox
from expenses.budget import Budget
from expenses.espense import Expense
from ui.views import ExpenseInputView, ExpenseListView, BudgetTrackingView


class UI:
    def __init__(self):
        self.budget = Budget(total_budget=5000)

        self.root = tk.Tk()
        self.root.title("Приложение для учета расходов")

        self.root.geometry("400x300")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.show_menu()

    def show_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        menu_label = tk.Label(self.main_frame, text="Выберите действие:")
        menu_label.pack()

        add_button = tk.Button(self.main_frame, text="Добавить расход",
                               command=self.add_expense)
        add_button.pack()

        view_button = tk.Button(self.main_frame, text="Просмотреть расходы",
                                command=self.view_expenses)
        view_button.pack()

        budget_button = tk.Button(self.main_frame, text="Отслеживание бюджета",
                                  command=self.budget_tracking)
        budget_button.pack()

    def add_expense(self):
        expense_details = ExpenseInputView.get_expense_details()

        category = self.budget.get_category(expense_details[2])
        if category is None:
            BudgetTrackingView.category_not_found()
            return

        expense = Expense(*expense_details, category)
        category.add_expense(expense)
        messagebox.showinfo("Добавление расхода", "Расход успешно добавлен.")

    def view_expenses(self):
        import tkinter.simpledialog
        category_name = tkinter.simpledialog.askstring("Просмотр расходов",
                                                       "Введите название категории (или оставьте пустым для просмотра всех расходов):")
        if category_name:
            category = self.budget.get_category(category_name)
            expenses = category.get_expenses() if category else []
        else:
            expenses = [expense for cat in self.budget.categories.values() for
                        expense in cat.get_expenses()]
        ExpenseListView.show_expenses(expenses)

    def budget_tracking(self):
        total_budget = self.budget.get_total_budget()
        remaining_budget = self.budget.get_remaining_budget()

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        total_budget_label = tk.Label(self.main_frame, text=f"Общий бюджет: {total_budget}")
        total_budget_label.pack()

        remaining_budget_label = tk.Label(self.main_frame, text=f"Остаток бюджета: {remaining_budget}")
        remaining_budget_label.pack()

        back_button = tk.Button(self.main_frame, text="Назад", command=self.show_menu)
        if back_button:
            back_button.pack()

    def run(self):
        self.root.mainloop()
