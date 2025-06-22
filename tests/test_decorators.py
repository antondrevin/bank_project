import pytest

from src.decorators import foo, log


def test_log_error_consol(capsys):

    foo

    with pytest.raises(TypeError):
        foo(5, "x")
    captured = capsys.readouterr()
    assert "foo - <class 'TypeError'> - args: (5, 'x'), kwargs: {}\n\n" == captured.out


def test_log_ok_file():
    file_name = "tests/testlog.txt"

    log(filename=file_name)

    resalt = foo(5, 6)
    assert resalt == 11

    with open(file_name, "r", encoding="utf-8") as f:
        write_file = f.readlines()
        assert write_file[-1] == "foo - OK - 11\n"
