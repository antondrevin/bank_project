import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        ("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6", "1234 56** **** 3456"),
        ("1 2 3 4 5 6 7 8 9 0", "введен не корректный номер карты"),
        (1234567890123456789, "введен не корректный номер карты"),
        ("qwertyuiopasdfgh", "номер карты должен состоять только из цифр"),
    ],
)
def test_get_mask_card_number(entry_value, expected):
    assert get_mask_card_number(entry_value) == expected


@pytest.mark.parametrize(
    "entry_value, expected",
    [
        (73654108430135874305, "**4305"),
        ("7 3 6 5 4 1 0 8 4 3 0 1 3 5 8 7 4 3 0 5", "**4305"),
        (73654108430135874305321635, "введен не корректный номер счета"),
        (736541084301358, "введен не корректный номер счета"),
        ("qwertyuiopasdfghjklz", "номер счета должен состоять только из цифр"),
    ],
)
def test_get_mask_account(entry_value, expected):
    assert get_mask_account(entry_value) == expected
