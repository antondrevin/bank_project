import os
import sys

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from generators import filter_by_currency  # type: ignore
from processing import filter_by_state, sort_by_date  # type: ignore
from read_csv_xls import read_csv, read_xls  # type: ignore
from utils import open_json, search_transaktion  # type: ignore
from widget import get_data, mask_account_card  # type: ignore


def main():
    user_input = input("""Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
- """)
    transactions_list = []
    while True:
        if user_input == "1":
            transactions_list = open_json("data/operation.json")
            print("Для обработки выбран JSON-файл")
            break
        elif user_input == "2":
            transactions_list = read_csv("data/transactions.csv")
            print("Для обработки выбран CSV-файл")
            break
        elif user_input == "3":
            transactions_list = read_xls("data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл")
            break
        else:
            user_input = input("не верный ввод, повторите")
    while True:
        user_input = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
- """).upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions_list = filter_by_state(transactions_list, key_state=user_input)
            print(f"Операции отфильтрованы по статусу {user_input}")
            break
        else:
            print(f"Статус операции {user_input} недоступен")

    user_input = input("Отсортировать операции по дате? Да/Нет - ").lower()

    if user_input == "да":
        while True:
            user_input = input("Отсортировать по возрастанию или по убыванию? - ").lower()
            if user_input == "по возрастанию":
                sorting = False
            elif user_input == "по убыванию":
                sorting = True
            else:
                print("не корректный ввод, попробуйте снова")
                continue
            transactions_list = sort_by_date(transactions_list, sorting=sorting)
            break

    user_input = input("Выводить только рублевые транзакции? Да/Нет - ").lower()

    if user_input == "да":
        transactions_list = list(filter_by_currency(transactions_list, "RUB"))

    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет - ").lower()
    if user_input == "да":
        user_input = input("введите фильтр - ")
        transactions_list = search_transaktion(transactions_list, user_input)

    len_transaktion = len(transactions_list)
    if len_transaktion == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций")
        print(f"Всего банковских операций в выборке: {len_transaktion}")
        for transaction in transactions_list:
            data_transaction = get_data(transaction["date"])
            print(f"{data_transaction} {transaction['description']}")
            card_to = mask_account_card(transaction["to"])
            if transaction["from"] == "":
                print(card_to)
            else:
                card_from = mask_account_card(transaction["from"])
                print(f"{card_from} -> {card_to}")
            print(f"Сумма: {transaction['amount']} {transaction['currency_code']}")
            print()


if __name__ == "__main__":
    main()
