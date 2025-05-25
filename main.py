import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from masks import get_mask_card_number, get_mask_account
from widget import mask_account_card, get_data

if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(get_data("2024-03-11T02:26:18.671407"))
