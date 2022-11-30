import math
from dataclasses import dataclass


def circle(radius):
    return math.pi * radius ** 2


circle_area = lambda radius: math.pi * radius ** 2

print(circle(42))
print(circle_area(42))

# @dataclass
# class Person:
#     age: int
#     weight: int
#     name: str
#
# people = Person()
#
#
# sorted(people, key=lambda person:person.age)

print(f"Wynik map: {list(map(lambda x: x ** 2, range(10)))}")
print(f"Wynik map 2: {list(map(print, range(5), range(4), range(5)))}")
# print(f"Wynik map: {(map(lambda x: x**2, range(10)))}")
evens = filter(lambda number: number % 2 == 0, range(10))
odds = filter(lambda number: number % 2 == 1, range(10))
print(list(evens))
print(list(odds))
persons = ["tomek", "jakub", 'tadeusz']
s = filter(lambda person: person.startswith('t'), persons)
print(list(s))
