import pytest
from src.widget import mask_account_card
from src.widget import get_data


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        ("блда бла 1234567891123456", "блда бла 1234 56** **** 3456"),
        ("блда бла 123456789112345s", "номер карты должен состоять только из цифр"),
        ("Счет 64686473678894779589", "счет **9589"),
        ("СЧЕТ 64686473678894779000", "счет **9000"),
        ("Счет 6468647367889477958X", "номер счета должен состоять только из цифр"),
        ("Счет 73678894779589", "введен не корректный номер счета"),
    ],
)
def test_mask_account_card(entry_value, expected):
    assert mask_account_card(entry_value) == expected


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"
