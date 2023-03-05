import csv
import time
from random import shuffle

from src.entity.student import Student
import src.services.algorithms as al
from src.services.tree import Tree


def prepare_data(to_shuffle: bool = False) -> list[Student]:
    reader = csv.DictReader
    data = Student.read_from_stream(filename='data/students_data.csv', reader=reader)
    if to_shuffle:
        shuffle(data)
    return data


def make_timer(callback, *args):
    start = time.perf_counter_ns()
    result = callback(*args)
    end = time.perf_counter_ns()
    print('Fail!', end=' ') if result is None else print('Success! ', end=' ')
    print(f"{callback.__name__}: Spent time {end - start} nanoseconds")
    return result


if __name__ == '__main__':
    students = prepare_data(True)
    sorted_students = sorted(students, key=lambda x: getattr(x, key))

    key = 'idnp'
    value = 9472599177802

    make_timer(al.sequential_search, value, students, key)

    tree = Tree(students[0])
    [tree.insert(student, key) for student in students[1:]]

    make_timer(tree.find_value, value, key)
    make_timer(al.binary_search, value, sorted_students, key)
    make_timer(al.fibonacci_method, value, sorted_students, key)
    if type(value) is str:
        sorted_students = sorted(students, key=lambda x: al.convert_value_to_int(getattr(x, key)))
    else:
        sorted_students = sorted(students, key=lambda x: getattr(x, key))
    res = make_timer(al.interpolation_search, value, sorted_students, key)
    if res is not None:
        Student.write_in_stream(res, 'data/result.csv', csv.DictWriter)
