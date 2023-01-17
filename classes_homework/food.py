class Ingredient:

    def __init__(self, name, protein, carbon, fat):
        self.fat = fat
        self.carbon = carbon
        self.protein = protein
        self.name = name

    def calc_calories(self, amount):
        return (amount / 100) * (self.protein * 4 + self.carbon * 4 + self.fat * 9.4)


class Meal:

    def __init__(self, name):
        self.name = name
        self.ingredients = {}

    def add_ingredients(self, ingredient, amount):
        protein = amount / 100 * ingredient.protein
        carbon = amount / 100 * ingredient.carbon
        fat = amount / 100 * ingredient.fat
        calories = ingredient.calc_calories(amount)
        self.ingredients[ingredient] = [amount, protein, carbon, fat, calories]


class DayPlan:

    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def show_summary(self):
        for meal in self.meals:
            print(f'Meal: {meal.name.title()}:')
            for ingredient, data in meal.ingredients.items():
                print(f'{data[0]}g {ingredient.name.title()} (protein: {data[1]}, carbon: {data[2]},'
                      f' fat: {data[3]}, calories: {data[4]})')


egg = Ingredient('egg', 13, 1.1, 11)
tomato = Ingredient('tomato', 0.9, 3.9, 0.2)

scrambled_eggs = Meal('scrambled_eggs')
scrambled_eggs.add_ingredients(egg, 200)
scrambled_eggs.add_ingredients(tomato, 50)

menu = DayPlan()
menu.add_meal(scrambled_eggs)
menu.show_summary()
