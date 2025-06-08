def get_mask_card_number(card_number: int | str) -> str:
    """Возвращает маску банковской карты: XXXX XX** **** XXXX."""
    card_number_str = str(card_number).replace(" ", "")
    if len(card_number_str) != 16:
        return "введен не корректный номер карты"
    elif not card_number_str.isdigit():
        return "номер карты должен состоять только из цифр"

    parts = [card_number_str[i:i + 4] for i in range(0, len(card_number_str), 4)]
    masked = " ".join(parts)
    masked_list = list(masked)

    for i in range(len(masked_list)):
        if 7 <= i <= 13 and masked_list[i] != " ":
            masked_list[i] = "*"
    return "".join(masked_list)


def get_mask_account(account_number: int | str) -> str:
    """Возвращает маску банковского счёта в формате: **XXXX."""
    account_number_str = str(account_number).replace(" ", "")
    if len(account_number_str) != 20:
        return "введен не корректный номер счета"
    elif not account_number_str.isdigit():
        return "номер счета должен состоять только из цифр"
    return "**" + account_number_str[-4:]
