from unittest.mock import mock_open, patch

from src.utils import open_json, summ_operation


def test_open_json():
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert open_json("") == {"1": "2"}
    with patch("builtins.open", mock_open(read_data='{"1":"2"')):
        assert open_json("") == []
    assert open_json("") == []


def test_summ_operation():
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 111}
        assert (summ_operation({
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}}}) == "сумма транзакции 111 рублей")
        assert (summ_operation({
            "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}) == "сумма транзакции 1000 рублей")
        assert summ_operation({}) == "не верный формат"
