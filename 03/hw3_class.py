from itertools import zip_longest

class CustomList(list):
    def __add__(self, other):
        return CustomList([x + y for x, y in zip_longest(self, other, fillvalue=0)])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return CustomList([x - y for x, y in zip_longest(self, other, fillvalue=0)])

    def __rsub__(self, other):
        return CustomList([y - x for x, y in zip_longest(self, other, fillvalue=0)])

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return sum(self) == sum(other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) > sum(other)
        return False

    def __ge__(self, other):
        if isinstance(other, CustomList):
            return sum(self) >= sum(other)
        return False

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) < sum(other)
        return False

    def __le__(self, other):
        if isinstance(other, CustomList):
            return sum(self) <= sum(other)
        return False

    def __str__(self):
        return f'{list(self)} sum={sum(self)}'
