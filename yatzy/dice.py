import random


class Die:
    """ Sets the do's and do not's of the die """

    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    # equals
    def __eq__(self, other):
        return int(self) == other

    # not equals
    def __ne__(self, other):
        return int(self) != other

    # greater than
    def __gt__(self, other):
        return int(self) > other

    # less than
    def __lt__(self, other):
        return int(self) < other

    # greater than or equal to
    def __ge__(self, other):
        return int(self) >= other or int(self) == other

    # less than or equal to
    def __le__(self, other):
        return int(self) <= other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    """ Inherates from Die and overrides the
        Init """
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
