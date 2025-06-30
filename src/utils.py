import json
from typing import Any

from src.external_api import converter


def open_json(path: str) -> Any:
    """Функция по заданному пути открывает json файл и возвращает его"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except Exception:
        return []


def summ_operation(operation: dict) -> str:
    """Функция возвращает сумму транзакции в рублях"""
    if operation != {}:
        code_currency = operation["operationAmount"]["currency"]["code"]
        amount = operation["operationAmount"]["amount"]
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return f"сумма транзакции {operation["operationAmount"]["amount"]} рублей"
        else:
            convert_currency = converter(code_currency, amount)
            return f"сумма транзакции {convert_currency} рублей"
    return "не верный формат"
