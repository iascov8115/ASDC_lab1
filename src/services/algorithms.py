from src.entity.student import Student


def sequential_search(value: int, array: list[Student], key: str) -> Student | None:
    for obj in array:
        if getattr(obj, key) == value:
            return obj
    return None


def binary_search(value: int, array: list[dict], key: str) -> dict | None:
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        mid_value = getattr(array[mid], key)
        if mid_value < value:
            low = mid + 1
        elif mid_value > value:
            high = mid - 1
        else:
            return array[mid]
    return None


def find_mid(low_val: int, high_val: int, value: int, low: int, high: int) -> int:
    return low + ((value - low_val) * (high - low)) // (high_val - low_val)


def interpolation_search(value: int, array: list[Student], key: str) -> Student | None:
    low, high = 0, len(array) - 1
    low_val, high_val = getattr(array[low], key), getattr(array[high], key)
    while low_val < value < high_val:
        if high_val == low_val:
            break
        mid = find_mid(low_val, high_val, value, low, high)
        mid_val = getattr(array[mid], key)
        if mid_val < value:
            low = mid + 1
            low_val = getattr(array[low], key)
        elif mid_val > value:
            high = mid - 1
            high_val = getattr(array[high], key)
        else:
            return array[mid]

    if low_val == value:
        return array[low]
    if high_val == value:
        return array[high]

    return None


def fibonacci_method(value: int | str, array: list[Student], key: str) -> Student | None:
    n = len(array)
    fib_m2 = 0
    fib_m1 = 1
    fib_m3 = fib_m2 + fib_m1

    while fib_m3 < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m3
        fib_m3 = fib_m2 + fib_m1
    offset = -1
    while fib_m3 > 1:
        i = min(offset + fib_m2, n - 1)
        if getattr(array[i], key) < value:
            fib_m3 = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m3 - fib_m1
            offset = i
        elif getattr(array[i], key) > value:
            fib_m3 = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m3 - fib_m1
        else:
            return array[i]

    if fib_m1 and array[n - 1] == value:
        return array[n - 1]

    return None
