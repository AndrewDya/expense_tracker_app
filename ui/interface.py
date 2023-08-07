import tkinter as tk


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Money stack")
        self.root.geometry("300x500")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.button_data = [
            ("Счета", self.choose_account),
            ("Расходы", self.choose_category),
            ("Операции", self.choose_operation),
            ("Обзор", self.browse_data)
        ]

        self.choose_account()

    def choose_account(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        balance_label = tk.Label(self.main_frame, text="Баланс: $5000",
                                 font=("Helvetica", 10, "bold"), anchor="w")
        balance_label.pack()

        card_category_label = tk.Label(self.main_frame,
                                       text="Банковские карты:",
                                       anchor="w")
        card_category_label.pack(side="top", anchor="w")

        add_card_button = tk.Button(
            self.main_frame, text="Добавить карту", anchor="w",
            # command=self.add_card,
            relief=tk.RAISED, pady=4, bg="lightyellow", fg="black",
            font=("Helvetica", 10)
        )
        add_card_button.pack(side="top", anchor="w", padx=6)

        account_category_label = tk.Label(self.main_frame, text="Счета:",
                                          anchor="w")
        account_category_label.pack(side="top", anchor="w")

        add_account_button = tk.Button(
            self.main_frame, text="Добавить счет", anchor="w",
            # command=self.add_account,
            relief=tk.RAISED, pady=4, bg="lightgreen", fg="black",
            font=("Helvetica", 10)
        )
        add_account_button.pack(side="top", anchor="w", padx=6)

        savings_category_label = tk.Label(self.main_frame, text="Сбережения:",
                                          anchor="w")
        savings_category_label.pack(side="top", anchor="w")

        add_savings_button = tk.Button(
            self.main_frame, text="Добавить сбережения", anchor="w",
            # command=self.add_savings,
            relief=tk.RAISED, pady=4, bg="lightpink", fg="black",
            font=("Helvetica", 10)
        )
        add_savings_button.pack(side="top", anchor="w", padx=6)

        tk.Frame(self.main_frame, height=10).pack()

        for text, command in self.button_data:
            button = tk.Button(
                self.main_frame, text=text, anchor="w", command=command,
                relief=tk.RAISED, pady=7, bg="lightblue", fg="black",
                font=("Helvetica", 10)
            )
            button.pack(side="left", padx=6)

    def choose_category(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.main_frame, text="Выберите категорию:",
                               font=("Helvetica", 10, "bold"))
        title_label.pack(padx=10, pady=10)

        categories = ["Еда", "Транспорт", "Развлечения", "Здоровье", "Одежда",
                      "Путешествия", "Образование", "Дом", "Техника", "Прочее"]

        for i in range(0, len(categories), 2):
            row_frame = tk.Frame(self.main_frame)
            row_frame.pack(fill="x", padx=10, pady=5)

            for j in range(2):
                index = i + j
                if index < len(categories):
                    category = categories[index]

                    button = tk.Button(
                        row_frame, text=category, anchor="center",
                        width=15,
                        command=lambda cat=category: self.category_selected(
                            cat),
                        relief=tk.RAISED, pady=8, bg="lightgreen", fg="black",
                        font=("Helvetica", 10, "bold")
                    )
                    button.pack(side="left", padx=8)

        for text, command in self.button_data:
            button = tk.Button(
                self.main_frame, text=text, anchor="w", command=command,
                relief=tk.RAISED, pady=7, bg="lightblue", fg="black",
                font=("Helvetica", 10)
            )
            button.pack(side="left", padx=7)

    def choose_operation(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.main_frame, text="Выберите операцию:",
                               font=("Helvetica", 10, "bold"))
        title_label.pack(padx=10, pady=10)

        operations = ["Зарплата", "Переводы", "Снятие наличных", "Возврат", "Другое"]

        for operation in operations:
            button = tk.Button(
                self.main_frame, text=operation, anchor="center",
                width=25,
                command=lambda op=operation: self.operation_selected(op),
                relief=tk.RAISED, pady=8, bg="lightgreen", fg="black",
                font=("Helvetica", 10, "bold")
            )
            button.pack(padx=10, pady=5)

        for text, command in self.button_data:
            button = tk.Button(
                self.main_frame, text=text, anchor="w", command=command,
                relief=tk.RAISED, pady=7, bg="lightblue", fg="black",
                font=("Helvetica", 10)
            )
            button.pack(side="left", padx=7)

    def browse_data(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.main_frame, text="Обзор данных за месяц:",
                               font=("Helvetica", 10, "bold"))
        title_label.pack(padx=10, pady=10)

        #TODO код для получения данных о расходах и доходах за календарный месяц

        # expenses_total = self.get_expenses_total()
        # income_total = self.get_income_total()

        expenses_label = tk.Label(self.main_frame,
                                  text="Расходы за месяц: $",
                                  # text=f"Расходы за месяц: ${expenses_total:.2f}",
                                  anchor="w", font=("Helvetica", 10))
        expenses_label.pack(anchor="w", padx=10, pady=5)

        income_label = tk.Label(self.main_frame,
                                text="Расходы за месяц: $",
                                # text=f"Доходы за месяц: ${income_total:.2f}",
                                anchor="w", font=("Helvetica", 10))
        income_label.pack(anchor="w", padx=10, pady=5)

        tk.Frame(self.main_frame, height=10).pack()

        for text, command in self.button_data:
            button = tk.Button(
                self.main_frame, text=text, anchor="w", command=command,
                relief=tk.RAISED, pady=7, bg="lightblue", fg="black",
                font=("Helvetica", 10)
            )
            button.pack(side="left", padx=6)

    def run(self):
        self.root.mainloop()
