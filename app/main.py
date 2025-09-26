from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args) -> None:
        if args in cache_store:
            result = cache_store[args]
            print("Getting from cache")
        else:
            result = func(*args)
            cache_store[args] = result
            print("Calculating new result")
        return result
    return inner
