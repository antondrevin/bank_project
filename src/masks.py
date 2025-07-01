import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/masks.log', "w", "utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int | str) -> str:
    """Возвращает маску банковской карты: XXXX XX** **** XXXX."""
    logger.info("запущена функция get_mask_card_number")
    card_number_str = str(card_number).replace(" ", "")
    if len(card_number_str) != 16:
        logger.error("ошибка: не корректный номер карты")
        return "введен не корректный номер карты"
    elif not card_number_str.isdigit():
        logger.error("ошибка: не корректный номер карты")
        return "номер карты должен состоять только из цифр"

    parts = [card_number_str[i : i + 4] for i in range(0, len(card_number_str), 4)]
    masked = " ".join(parts)
    masked_list = list(masked)

    for i in range(len(masked_list)):
        if 7 <= i <= 13 and masked_list[i] != " ":
            masked_list[i] = "*"
    logger.info("вернулся замаскированный номер карты")
    return "".join(masked_list)


def get_mask_account(account_number: int | str) -> str:
    logger.info("запущена функция get_mask_account")
    """Возвращает маску банковского счёта в формате: **XXXX."""
    account_number_str = str(account_number).replace(" ", "")
    if len(account_number_str) != 20:
        logger.error("ошибка: некорректный номер карты")
        return "введен не корректный номер счета"
    elif not account_number_str.isdigit():
        logger.error("ошибка: некорректный номер карты")
        return "номер счета должен состоять только из цифр"
    logger.info("вернулся замаскированный номер счета")
    return "**" + account_number_str[-4:]
