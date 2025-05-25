import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(73654108430135874305))
