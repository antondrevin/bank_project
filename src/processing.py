def filter_by_state(list_state, key_state = "EXECUTED"):
    total_state = []
    for i in list_state:
        if i["state"] == key_state:
            total_state.append(i)

    return total_state


def sort_by_date(list_state, sorting = True):
    sorted_state = sorted(list_state, key=lambda x: x.get("date"), reverse=sorting)

    return sorted_state
