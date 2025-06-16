from typing import Callable, Any
from functools import wraps


def strict(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any) -> int:
        for type, arg in zip(func.__annotations__.values(), args):
            if not isinstance(arg, type):
                raise TypeError
            
        return func(*args)
    return wrapper


@strict
def add(a: int, b: int) -> int:
    return a + b

@strict
def something(a: list, b: dict, c: str) -> int:
    return len(a) + len(b) + len(c)


if __name__ == '__main__':
    print(add(2, 3))
    print(something([], {}, ''))
