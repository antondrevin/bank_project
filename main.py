import os
import sys

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from generators import card_number_generator, filter_by_currency, transaction_descriptions  # type: ignore
from masks import get_mask_account, get_mask_card_number  # type: ignore[attr-defined]
from processing import filter_by_state, sort_by_date  # type: ignore
from widget import get_data, mask_account_card  # type: ignore

state_opration = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Счет 6468647367889477958X"))
    print(mask_account_card("Счет 600000004686473678894779589"))
    print(mask_account_card("Счет 73678894779589"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_data("2024-03-11T02:26:18.671407"))
    print(filter_by_state(state_opration))
    print(filter_by_state(state_opration, key_state="CANCELED"))
    print(sort_by_date(state_opration))
    print(sort_by_date(state_opration, sorting=False))

    gen_usd = filter_by_currency(transactions, "USD")
    gen_rub = filter_by_currency(transactions, "RUB")
    gen_descript = transaction_descriptions(transactions)

    for _ in range(2):
        print(next(gen_usd))

    for _ in range(2):
        print(next(gen_rub))

    for _ in range(4):
        print(next(gen_descript))

    for card_number in card_number_generator(77777, 77779):
        print(card_number)
