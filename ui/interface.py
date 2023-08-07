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
            ("Категория", self.choose_category),
            ("Операция", self.choose_operation),
            ("Обзор", self.browse_data)
        ]

        self.choose_account()

    def choose_account(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        balance_label = tk.Label(self.main_frame, text="Баланс: $5000",
                                 font=("Helvetica", 10, "bold"), anchor="w")
        balance_label.pack()

        account_category_label = tk.Label(self.main_frame, text="Счета:",
                                          anchor="w")
        account_category_label.pack(side="top", anchor="w")

        savings_category_label = tk.Label(self.main_frame, text="Сбережения:",
                                          anchor="w")
        savings_category_label.pack(side="top", anchor="w")

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
        pass

    def browse_data(self):
        pass

    def run(self):
        self.root.mainloop()
