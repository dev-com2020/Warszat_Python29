from dataclasses import dataclass, field


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         '''dodawanie dwóch wektorów za pomocą +'''
#         return Vector(
#             self.x + other.x,
#             self.y + other.y,
#         )
#
#     def __sub__(self, other):
#         '''odejmowanie dwóch wektorów za pomocą -'''
#         return Vector(
#             self.x - other.x,
#             self.y - other.y,
#         )
#
#     def __repr__(self):
#         '''zwracanie tekstowej reprezentacji wektora'''
#         return f"<Wektor: x={self.x}, y={self.y}>"
#
#     def __eq__(self, other):
#         '''sprawdzanie czy dwa wektory są równe'''
#         return self.x == other.x and self.y == other.y


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        '''dodawanie dwóch wektorów za pomocą +'''
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        '''odejmowanie dwóch wektorów za pomocą -'''
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int

    def __add__(self, other):
        '''dodawanie dwóch wektorów za pomocą +'''
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        '''odejmowanie dwóch wektorów za pomocą -'''
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass
class DataClassWithDefaults:
    immutable: str = field(default="Statyczna wartość domyślna")
    mutable: list = field(default_factory=list)


print(DataClassWithDefaults())
print(DataClassWithDefaults("Jakieś niemodyfikowalne dane"))
print(DataClassWithDefaults(None, ['tomek', 'krzysiek']))
print(DataClassWithDefaults(mutable=['tomek', 'krzysiek'], immutable="Test"))

# print(Vector(2, 3))
# print(Vector(5, 3) + Vector(1, 2))
# print(Vector(5, 3) - Vector(1, 2))
# print(Vector(5, 3) == Vector(1, 2))
# print(Vector(1, 2) == Vector(1, 2))
# print()
# print(FrozenVector(2, 3))
# print(FrozenVector(5, 3) + FrozenVector(1, 2))
# print(FrozenVector(5, 3) - FrozenVector(1, 2))
# print(FrozenVector(5, 3) == FrozenVector(1, 2))
# print(FrozenVector(1, 2) == FrozenVector(1, 2))
