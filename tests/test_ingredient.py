import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    #Получить стоимость ингредиента
    def test_get_price(self):
        ingredient = Ingredient('SAUCE', "chili sauce", 300)
        assert ingredient.get_price() == 300

    #Получить название ингредиента
    def test_get_name(self):
        ingredient = Ingredient('SAUCE', "chili sauce", 300)
        assert ingredient.get_name() == "chili sauce"

    #Получить тип ингредиента
    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, "chili sauce", 300)
        assert ingredient.get_type() == type_ingredient