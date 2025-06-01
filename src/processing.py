def filter_by_state(list_state: list[dict], key_state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует словари по состоянию операции: выполнена/отменена"""
    total_state = []
    for i in list_state:
        if i["state"] == key_state:
            total_state.append(i)

    return total_state


def sort_by_date(list_state: list[dict], sorting: bool = True) -> list[dict]:
    """функция сортирует по дате операции"""
    sorted_state = sorted(list_state, key=lambda x: x.get("date"), reverse=sorting)

    return sorted_state
