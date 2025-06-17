from typing import Callable, Any
from functools import wraps


def strict(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> int:
        # check args annotations
        for type, arg in zip(func.__annotations__.values(), args):
            if not isinstance(arg, type):
                raise TypeError
        
        # check kwargs annotations
        for kwarg, value in kwargs.items():
            if not isinstance(value, func.__annotations__[kwarg]):
                raise TypeError 
            
        return func(*args)
    return wrapper


@strict
def add(a: int, b: int) -> int:
    return a + b

@strict
def something(a: list, b: dict, c: str) -> int:
    return len(a) + len(b) + len(c)

@ strict
def something_with_kwargs(a: int, g: None | int = None, c: set | dict = {}):
    return (a + g + len(c)) if g and c else a


if __name__ == '__main__':
    print(add(2, 3))
    print(something([], {}, ''))
    print(something_with_kwargs(1, g=2, c={3, 4}))
