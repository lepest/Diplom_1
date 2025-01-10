from praktikum.bun import Bun
from praktikum.burger import Burger
from data import Data
from praktikum.ingredient import Ingredient

class TestBurger:

    #Выбор булочек
    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(Data.bun)
        assert burger.bun == Data.bun

    #Добавление ингредиентов в список
    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingredient_1)
        assert burger.ingredients == [Data.ingredient_1]

    #удаление одного ингредиента из списка
    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingredient_1)
        burger.add_ingredient(Data.ingredient_2)
        list_ingredients = burger.ingredients
        index_ingredient = list_ingredients.index(Data.ingredient_1)
        burger.remove_ingredient(index_ingredient)
        assert list_ingredients == [Data.ingredient_2]

    #удаление всех ингредиентов из списка
    def test_remove_all_ingredients(self):
        burger = Burger()
        burger.add_ingredient(Data.ingredient_1)
        burger.add_ingredient(Data.ingredient_2)
        list_ingredients = burger.ingredients
        index_ingredient_1 = list_ingredients.index(Data.ingredient_1)
        burger.remove_ingredient(index_ingredient_1)
        index_ingredient_2 = list_ingredients.index(Data.ingredient_2)
        burger.remove_ingredient(index_ingredient_2)
        assert list_ingredients == []

    #Перемещение ингредиентов
    def test_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Data.ingredient_1)
        burger.add_ingredient(Data.ingredient_2)
        burger.add_ingredient(Data.ingredient_3)
        list_ingredients = burger.ingredients
        index_ingredient: int = list_ingredients.index(Data.ingredient_1)
        burger.move_ingredient(index_ingredient, index_ingredient-1)
        assert list_ingredients == [Data.ingredient_2, Data.ingredient_1, Data.ingredient_3]

    # Проверить стоимость бургера
    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient('SAUCE', "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 300

    #Получить квитанцию
    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient('SAUCE', "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert burger.get_receipt() == ('(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 300')
