from unittest.mock import mock_open, patch

from src.utils import open_json, process_bank_operations, search_transaktion, summ_operation


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


def test_search_transaktion(transactions_currency):
    assert search_transaktion(transactions_currency, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]


def test_process_bank_operations(transactions_currency):
    assert process_bank_operations(transactions_currency, [
        "Перевод организации", "Перевод со счета на счет"]) == {
        'Перевод организации': 2, 'Перевод со счета на счет': 2}
