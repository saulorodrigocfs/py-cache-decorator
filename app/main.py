from typing import Callable


def cache(func: Callable) -> Callable:
    memoria = {}

    def inner(*args, **kwargs) -> None:
        if args in memoria:
            result = memoria[args]
            print("Getting from cache")
        else:
            result = func(*args, **kwargs)
            memoria[args] = result
            print("Calculating new result")
        return result
    return inner
