from src.generators import filter_by_currency, transaction_descriptions, card_number_generator



def test_filter_by_currency(transactions_currency):
    gen_usd = filter_by_currency(transactions_currency, "USD")
    gen_rub = filter_by_currency(transactions_currency, "RUB")
    assert next(gen_usd) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {
        'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}
    }, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
    assert next(gen_usd) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {
        'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}
    }, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
    assert next(gen_rub) == {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {
        'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}
    }, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}
    assert next(gen_rub) == {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {
        'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}
    }, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}

def test_transaction_descriptions(transactions_currency):
    gen_descript = transaction_descriptions(transactions_currency)
    assert next(gen_descript) == "Перевод организации"
    assert next(gen_descript) == "Перевод со счета на счет"
    assert next(gen_descript) == "Перевод со счета на счет"
    assert next(gen_descript) == "Перевод с карты на карту"

def test_card_number_generator():
    gen_number_1 = card_number_generator(1, 3)
    gen_number_2 = card_number_generator(77777, 77779)
    assert next(gen_number_1) == "0000 0000 0000 0001"
    assert next(gen_number_1) == "0000 0000 0000 0002"
    assert next(gen_number_2) == "0000 0000 0007 7777"
    assert next(gen_number_2) == "0000 0000 0007 7778"
