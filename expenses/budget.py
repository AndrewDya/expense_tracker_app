class Budget:
    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.categories = {}

    def add_category(self, category):
        self.categories[category.name] = category

    def get_category(self, category_name):
        return self.categories.get(category_name)

    def get_total_budget(self):
        return self.total_budget

    def get_remaining_budget(self):
        total_expenses = sum(category.get_total_expenses() for category in self.categories.values())
        remaining_budget = self.total_budget - total_expenses
        return remaining_budget

    def __str__(self):
        return f"Total Budget: {self.total_budget}"
