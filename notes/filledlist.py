import copy


class FilledList(list):
    """ Fill a list using classes"""
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))
