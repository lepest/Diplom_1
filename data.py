from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class Data:
    ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    ingredient_3 = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)

    bun = Bun("black bun", 100)

    list_ingredient = (ingredient_1, ingredient_2, ingredient_3)