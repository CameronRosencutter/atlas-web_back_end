#!/usr/bin/env python3
'''Add 2 different numbers.'''

def add(a: float, b: float) -> float:
    result = a + b
    return result

a = 4
b = 3
result_sum = add(a, b)
print(f"{a} and {b} equals... {result_sum}")