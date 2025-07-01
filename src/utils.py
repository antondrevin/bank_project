import json
import logging
from typing import Any

from src.external_api import converter

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def open_json(path: str) -> Any:
    """Функция по заданному пути открывает json файл и возвращает его"""
    logger.info("запущена функция open_json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            logger.info("открыт файл")
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"ошибка {e}")
        return []
    except Exception as e:
        logger.error(f"ошибка {e}")
        return []


def summ_operation(operation: dict) -> str:
    """Функция возвращает сумму транзакции в рублях"""
    if operation != {}:
        code_currency = operation["operationAmount"]["currency"]["code"]
        amount = operation["operationAmount"]["amount"]
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("возврат суммы транзакции в рублях")
            return f"сумма транзакции {operation["operationAmount"]["amount"]} рублей"
        else:
            convert_currency = converter(code_currency, amount)
            logger.info("возврат конвертированной суммы транзакции в рублях")
            return f"сумма транзакции {convert_currency} рублей"
    logger.error("ошибка формата")
    return "не верный формат"
