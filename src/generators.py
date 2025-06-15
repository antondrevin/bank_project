from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict[Any, Any]]:
    """Функция возвращает итератор, который поочередно выдает транзакции с соответствующей валютой."""
    for i in transactions_list:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transactions_list: list[dict]) -> Generator[list]:
    """Функция возвращает описание каждой операции по очереди"""
    for i in transactions_list:
        yield i["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Функция возвращает номера банковских карт в формате: `XXXX XXXX XXXX XXXX` где X — цифра номера карты"""
    for i in range(start, end + 1):
        card_number = f"{i:016d}"
        card_number_str = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield card_number_str
