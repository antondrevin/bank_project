from typing import Generator

def filter_by_currency(transactions_list, currency) -> Generator[list]:
    for i in transactions_list:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i



def transaction_descriptions(transactions_list) -> Generator[list]:
    for i in transactions_list:
        yield i['description']


def card_number_generator(start, end) -> Generator[str]:
    for i in range(start, end + 1):
        card_number = f"{i:016d}"
        card_number_str = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
        yield card_number_str

