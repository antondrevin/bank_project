from typing import Any, Callable, Optional


def write_log(message: str, filename: Optional[str]) -> None:
    """функция записывает результат выполнения функции foo в файл"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message)


def log(filename: Optional[str] = None) -> Callable:
    """декоратор для логирования с настройками"""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                resalt = func(*args, **kwargs)
                message = f"{func.__name__} - OK - {resalt}\n"
                write_log(message, filename)
                return resalt
            except Exception as e:
                message = f"{func.__name__} - {type(e)} - args: {args}, kwargs: {kwargs}\n"
                write_log(message, filename)
                raise

        return wrapper

    return decorator


@log()
def foo(x: int, y: int) -> int:
    return x + y
