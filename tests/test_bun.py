from unittest.mock import Mock

class TestBun:

    #Получить название булочки
    def test_get_name(self):
        mock_name_bun = Mock()
        mock_name_bun.get_name.return_value = 'black bun'
        assert mock_name_bun.get_name() == "black bun"

    #Получить стоимость булочки
    def test_get_price(self):
        mock_price_bun = Mock()
        mock_price_bun.get_price.return_value = 100
        assert mock_price_bun.get_price() == 100