class ReversedStr(str):
    """ Reverses a string """
    def __new__(self,*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
