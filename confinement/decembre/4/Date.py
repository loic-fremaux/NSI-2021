from __future__ import annotations


class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return str(self.year) + "/" + str(self.month) + "/" + str(self.day)

    def __eq__(self, o: Date) -> bool:
        return self.year == o.year and self.month == o.month and self.day == o.day

    def __ne__(self, o: Date) -> bool:
        return not self.__eq__(o)

    def __gt__(self, other: Date) -> bool:
        return self.compare(other, lambda a, b: a > b)

    def __ge__(self, other: Date) -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __lt__(self, other: Date) -> bool:
        return self.compare(other, lambda a, b: a < b)

    def __le__(self, other: Date) -> bool:
        return self.__eq__(other) or self.__lt__(other)

    def compare(self, other: Date, calc) -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return False
                else:
                    return calc(self.day, other.day)
            else:
                return calc(self.month, other.month)
        else:
            return calc(self.year, other.year)

    def duree(self, other: Date) -> int:
        return abs((self.year - other.year)) * 365 + abs((self.month - other.month)) * 30 + abs((self.day - other.day))


# TESTS
d1 = Date(2020, 12, 25)
d2 = Date(2020, 12, 3)
d3 = Date(2020, 12, 3)
d4 = Date(2022, 12, 3)

# 2
print(d1.__lt__(d2))  # False
print(d1.__gt__(d2))  # True
print(d2.__gt__(d3))  # False
print(d2.__ge__(d3))  # True

# 3
print(d1.__str__())
print(d2.__str__())

# 4
print(d1.duree(d2))  # 22
print(d2.duree(d1))  # 22
print(d1.duree(d4))  # 752
