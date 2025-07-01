from unittest.mock import patch

from src.external_api import converter


def test_converter():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 7800.01}
        result = converter("USD", "100")
        assert result == 7800.01
