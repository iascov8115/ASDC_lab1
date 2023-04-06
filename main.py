import csv
import time
from random import shuffle

from src.entity.student import Student
import src.services.algorithms as al
from src.services.tree import TreeNode


def prepare_data(to_shuffle: bool = False) -> list[Student]:
    reader = csv.DictReader
    data = Student.read_from_stream(filename='public/students_data.csv', reader=reader)
    if to_shuffle:
        shuffle(data)
    return data


def make_timer(callback, *args):
    start = time.perf_counter_ns()
    result = callback(*args)
    end = time.perf_counter_ns()
    print('Fail!', end=' ') if result is None else print('Success! ', end=' ')
    print(f"{callback.__name__}: Spent time {end - start:,} nanoseconds")
    return result


def convert_value_to_int(obj: Student, key: str) -> Student:
    v = getattr(obj, key)
    nv = int.from_bytes(v.encode(), byteorder='big')
    setattr(obj, key, nv)
    return obj


def convert_value_to_str(obj: Student, key: str) -> Student:
    v = getattr(obj, key)
    nv = v.to_bytes((v.bit_length() + 7) // 8, 'big').decode()
    setattr(obj, key, nv)
    return obj


if __name__ == '__main__':
    key = 'firstname'
    value = 'Katerine'

    students = prepare_data(True)
    sorted_students = sorted(students, key=lambda x: getattr(x, key))

    make_timer(al.sequential_search, value, students, key)
    make_timer(al.sequential_search, value, sorted_students, key)

    tree = TreeNode(students[0])
    [tree.insert(student, key) for student in students[1:]]

    make_timer(tree.tree_search, value, key)
    make_timer(al.binary_search, value, sorted_students, key)
    make_timer(al.fibonacci_method, value, sorted_students, key)

    new_value = 0
    if type(value) is str:
        new_value = int.from_bytes(value.encode(), byteorder='big')
        students = [convert_value_to_int(student, key) for student in students]
        sorted_students = sorted(students, key=lambda x: getattr(x, key))
    else:
        new_value = value
        sorted_students = sorted(students, key=lambda x: getattr(x, key))

    res = make_timer(al.interpolation_search, new_value, sorted_students, key)

    if res is not None:
        if type(value) is str:
            convert_value_to_str(res, key)
        Student.write_in_stream([res], csv.DictWriter, 'public/result.csv')
