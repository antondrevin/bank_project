from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: str) -> str:
    """принимает катру/счет, возвращает тип карты/счет и замаскированый номер карты/счета"""
    if "счет" in name_card.lower():
        if len(name_card[5:]) == 20:
            number_card = name_card[-20:]
            mask_card = get_mask_account(number_card)
            if number_card.isdigit():
                resalt = f"счет {mask_card}"
            else:
                return "номер счета должен состоять только из цифр"
        else:
            return "введен не корректный номер счета"

    else:
        if len(name_card) > 16:
            type_card = name_card[:-16]
            number_card = name_card[-16:]
            mask_card = get_mask_card_number(number_card)
            if number_card.isdigit():
                return f"{type_card}{mask_card}"
            else:
                return "номер карты должен состоять только из цифр"
    return resalt


def get_data(time_card: str) -> str:
    """принимает системную дату/время, возвращает дату в формате ДД.ММ.ГГГГ"""
    return time_card[8:10] + "." + time_card[5:7] + "." + time_card[:4]
