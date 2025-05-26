from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(name_card: str) -> str:
    '''принимает катру/счет, возвращает тип карты/счет и замаскированый номер карты/счета'''
    if "счет" in name_card.lower():
        number_card = name_card[-20:]
        mask_card = get_mask_account(number_card)
        return f"счет {mask_card}"

    else:
        type_card = name_card[:-16]
        number_card = name_card[-16:]
        mask_card = get_mask_card_number(number_card)
        return f"{type_card} {mask_card}"


def get_data(time_card: str) -> str:
    '''принимает системную дату/время, возвращает дату в формате ДД.ММ.ГГГГ'''
    return time_card[8:10] + "." + time_card[5:7] + "." + time_card[:4]
