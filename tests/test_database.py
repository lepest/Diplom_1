from unittest.mock import Mock
from praktikum.database import Database

class TestDatabase:

    #Получить список доступных булок
    def test_available_buns(self):
        database = Database()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "mushroom sauce"
        mock_bun.get_price.return_value = 400
        database.buns.append(mock_bun)
        list_buns = database.available_buns()
        assert mock_bun in list_buns

    #Получить список доступных ингредиентов
    def test_available_ingredients(self):
        database = Database()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "cheese"
        mock_ingredient.get_price.return_value = 400
        database.ingredients.append(mock_ingredient)
        list_ingredients = database.available_ingredients()
        assert mock_ingredient in list_ingredients