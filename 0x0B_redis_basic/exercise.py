#!/usr/bin/env python3
"""
Main file
"""

import uuid
import redis
from typing import Union, Callable
from functools import wraps

class Cache:
    """This is the class cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"
            self._redis.rpush(input_key, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(output_key, str(output))
            return output
        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)

    def replay(self, method: Callable):
        method_name = method.__qualname__
        input_key = f"{method_name}:inputs"
        output_key = f"{method_name}:outputs"

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        num_calls = len(inputs)
        print(f"{method_name} was called {num_calls} times:")
        for input_data, output_data in zip(inputs, outputs):
            input_str = input_data.decode('utf-8')
            output_str = output_data.decode('utf-8')
            print(f"{method_name}(*{input_str}) -> {output_str}")


# Test cases
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

# Example usage of replay
cache.replay(cache.store)
