from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(operation, state_CANCELED, state_EXECUTED):
    assert filter_by_state(operation, key_state="CANCELED") == state_CANCELED
    assert filter_by_state(operation, key_state="EXECUTED") == state_EXECUTED


def test_sort_by_date(operation, date_true, date_false):
    assert sort_by_date(operation, sorting=True) == date_true
    assert sort_by_date(operation, sorting=False) == date_false
